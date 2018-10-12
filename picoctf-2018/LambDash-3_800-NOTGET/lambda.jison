/* description: Parses end executes mathematical expressions. */

/* lexical grammar */
%lex

%%
\s+                 /* skip whitespace */
"lambda"	        return "LAMBDA";
"fix"               return "FIX";
"LAMBDA"            return "TYPE_LAMBDA";
"as"                return "AS";
"returns"           return "RETURNS";
"alias"             return "ALIAS";
"forall"            return "FORALL";
"="                 return "=";
"in"                return "IN";

"("				    return "(";
")"				    return ")";
"["                 return "[";
"]"                 return "]";
"<"                 return "<";
">"                 return ">";
"{"                 return "{";
"}"                 return "}";
","                 return ",";

"+"				    return "+";
"*"				    return "*";

":"				    return ":";
"->"			    return "->";
"int"               return "INT";

"fold"              return "FOLD";
"unfold"            return "UNFOLD";

"rec"               return "REC";

"case"              return "CASE";
"|"                 return "|";

"#"                 return "#";

"unit"              return "UNIT";
[0-9]+\b            return "NUMERAL";
\`[a-zA-Z0-9_]+\b   return "LABEL";
[a-zA-Z_]+\b        return "IDENT";
"."                 return "DOT";

<<EOF>>			    return "EOF";

/lex

/* operator associations and precedence */

%left MEXP_TO_EXP GENERICIZE
%left DOT LAMBDA TYPE_LAMBDA FIX ALIAS
%left NUMERAL LABEL IDENT
%left CASE
%left '+'
%left '*'
%right '->'
%left '(' ')' '[' ']' '{' '}' '<' '>'
%left CALL FOLD UNFOLD
%left '#'
%left ':'

%start expressions

%% /* language grammar */

expressions
    : e EOF
        {require("util").inspect.defaultOptions.depth=1000; console.log($1); return $1;}
    ;

untyped_ident
    : IDENT
        {$ = yytext;}
    ;

ident
    : untyped_ident ":" type %prec GENERICIZE
        {$ = { kind: "TYPED_IDENT", type: $3, value: $1 };}
    | untyped_ident
        {$ = { kind: "UNTYPED_IDENT", value: $1};}
    ;

label
    : LABEL
        {$ = (yytext).slice(1);}
    ;

tuple_element
    : label e
        { $={ label: $1, value: $2 };}
    ;

tuple_contents
    : tuple_element
        {$ = [$1];}
    | tuple_contents "," tuple_element
        {$ = [...($1), $3] }
    ;

tuple
    : "{" tuple_contents "}"
        {$=$2;}
    ;

case_entry
    : label ident "->" e
        {$ = { label: $1, binding: $2, value: $4 };}
    ;

case_entry_list
    : case_entry "|" case_entry
        {$ = [$1, $3 ];}
    | case_entry_list "|" case_entry
        {$ = [...($1), $3] }
    ;

case
    : CASE "(" mexp ")" "{" case_entry_list "}"
        {$ = { kind:"CASE", binding: $3, value: $6};}
    ;

e
    : e "+" e
        {$ = { kind: "PLUS", value: [$1, $3] };}
    | e "*" e
        {$ = { kind: "TIMES", value: [$1, $3] };}
    | mexp %prec MEXP_TO_EXP
        {$ = $1;}
    ;


mexp
    : ALIAS untyped_ident "=" type IN e
        {$ = { kind: "ALIAS", value: $6, ident: $2, type: $4};}
    | mexp mexp %prec CALL
        {$ = { kind: "CALL", value: $1, subst: $2 };}
    | "(" e ")"
        {$ = $2;}
    | mexp "[" type "]" %prec CALL
        {$ = { kind: "TYPE_CALL", value: $1, subst: $3};}
    | FOLD AS type mexp
        {$ = { kind: "FOLD", value: $4, type: $3};}
    | UNFOLD mexp
        {$ = { kind: "UNFOLD", value: $2};}
    | LAMBDA ident DOT e
        {$ = { kind: "LAMBDA", value: $4, binding: $2 };}
    | TYPE_LAMBDA untyped_ident DOT e
        {$ = { kind: "TYPE_LAMBDA", value: $4, binding: $2};}
    | FIX untyped_ident ident RETURNS type DOT e
        {$ = { kind: "FIXED", fn: $2, value: $7, returnType: $5, binding: $3};}
    | ident
        {$ = $1}
    | tuple
        {$ = { kind: "TUPLE", value: $1 };}
    | mexp "#" label %prec CALL
        {$ = { kind: "EXTRACT", value: $1, productLabel: $3 };}
    | NUMERAL
        {$ = { kind: "NUMBER", value: Number(yytext) };}
    | "(" ")"
        {$ = { kind: "UNIT" };}
    | case
        {$ = $1;}
    | label e AS type %prec CALL
        {$ = { kind: "SUM", sumLabel: $1, value: $2, type: $4 };}
    ;


label_type_single
    : label type
        {$ = { label: $1, value: $2 };}
    ;

sum_type
    : label_type_single
        {$ = [$1]}
    | sum_type "+" label_type_single
        {$ = [...($1), $3] }
    ;

product_type
    : label_type_single
        {$ = [$1]}
    | product_type "*" label_type_single
        {$ = [...($1), $3] }
    ;

type
    : INT
        {$ = { kind: "INT" };}
    | UNIT
        {$ = { kind: "UNIT" };}
    | untyped_ident
        {$ = { kind: "TYPE_VAR", value: $1};}
    | "<" sum_type ">" %prec "+"
        {$ = { kind: "SUM", value: $2 };}
    | "{" product_type "}" %prec "*"
        {$ = { kind: "PRODUCT", value: $2 };}
    | type "->" type
        {$ = { kind: "ARROW", value: [$1, $3] };}
    | REC untyped_ident DOT type
        {$ = { kind: "REC", value: $4, binding: $2};}
    | FORALL untyped_ident DOT type
        {$ = { kind: "NEEDS_CONSTRAINT", binding: $2, type: $4};}
    | "(" type ")"
        {$ = $2}
    ;
