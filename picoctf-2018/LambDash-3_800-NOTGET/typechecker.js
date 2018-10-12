"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const immutable_1 = require("immutable");
let getType = function (t, gamma) {
    if (t.kind === "TYPE_VAR") {
        let result = gamma.get(t.value);
        if (result === undefined) {
            throw new TypeError(`Cannot find variable ${t.value}`);
        }
        if (result.kind === "UNKNOWN") {
            return t;
        }
        else {
            return result;
        }
    }
    else {
        return t;
    }
};
exports.typeToString = function (type) {
    switch (type.kind) {
        case "UNIT": {
            return "UNIT";
        }
        case "INT": {
            return "INT";
        }
        case "TYPE_VAR": {
            return type.value;
        }
        case "SUM": {
            return `<${type.value.map(({ label, value }) => `\`${label} ${exports.typeToString(value)}`).join(" + ")}>`;
        }
        case "PRODUCT": {
            return `{${type.value.map(({ label, value }) => `\`${label} ${exports.typeToString(value)}`).join(" * ")}}`;
        }
        case "ARROW": {
            return `(${exports.typeToString(type.value[0])} -> ${exports.typeToString(type.value[1])})`;
        }
        case "REC": {
            return `rec ${type.binding}.${exports.typeToString(type.value)}`;
        }
        case "NEEDS_CONSTRAINT": {
            return `∀ ${type.binding}.${exports.typeToString(type.type)}`;
        }
    }
};
exports.eToString = function (e) {
    switch (e.kind) {
        case "TYPED_IDENT": {
            return `${e.value}:${exports.typeToString(e.type)}`;
        }
        case "UNTYPED_IDENT": {
            return e.value;
        }
        case "LAMBDA": {
            return `lambda ${exports.eToString(e.binding)}.${exports.eToString(e.value)}`;
        }
        case "TYPE_LAMBDA": {
            return `LAMBDA ${e.binding}.${exports.eToString(e.value)}`;
        }
        case "FIXED": {
            return `fix ${e.fn} ${exports.eToString(e.binding)} returns ${exports.typeToString(e.returnType)}. ${exports.eToString(e.value)}`;
        }
        case "CALL": {
            return `(${exports.eToString(e.value)}) ${exports.eToString(e.subst)}`;
        }
        case "TYPE_CALL": {
            return `(${exports.eToString(e.value)}) [${exports.typeToString(e.subst)}]`;
        }
        case "FOLD": {
            return `fold as ${exports.typeToString(e.type)} ${exports.eToString(e.value)}`;
        }
        case "UNFOLD": {
            return `unfold ${exports.eToString(e.value)}`;
        }
        case "TUPLE": {
            return `(${e.value.map(({ label, value }) => `\`${label} ${exports.eToString(value)}`).join(", ")})`;
        }
        case "SUM": {
            return `\`${e.sumLabel} ${exports.eToString(e.value)} as ${exports.typeToString(e.type)}`;
        }
        case "EXTRACT": {
            return `(${exports.eToString(e.value)})#\`${e.productLabel}`;
        }
        case "CASE": {
            return `case (${exports.eToString(e.binding)}) {${e.value.map(({ label, value, binding }) => `\`${label} ${exports.eToString(binding)} -> ${exports.eToString(value)}`).join(" | ")}}`;
        }
        case "PLUS": {
            return `${exports.eToString(e.value[0])} + ${exports.eToString(e.value[1])}`;
        }
        case "TIMES": {
            return `${exports.eToString(e.value[0])} * ${exports.eToString(e.value[1])}`;
        }
        case "NUMBER": {
            return `${e.value}`;
        }
        case "UNIT": {
            return `()`;
        }
    }
};
let typeSubst = function (replacee, original, replacement, gamma) {
    replacee = getType(replacee, gamma);
    let subst = (current, gamma) => {
        current = getType(current, gamma);
        if (typesAreEqual(replacee, current, gamma)) {
            return replacement;
        }
        switch (current.kind) {
            case "UNIT":
            case "INT":
            case "TYPE_VAR": {
                return current;
            }
            case "SUM": {
                let newValues = current.value.map(({ label, value }) => ({ label, value: subst(value, gamma) }));
                return { kind: "SUM", value: newValues };
            }
            case "PRODUCT": {
                let newValues = current.value.map(({ label, value }) => ({ label, value: subst(value, gamma) }));
                return { kind: "PRODUCT", value: newValues };
            }
            case "ARROW": {
                return { kind: "ARROW", value: [
                        subst(current.value[0], gamma),
                        subst(current.value[1], gamma),
                    ] };
            }
            case "REC": {
                return {
                    kind: "REC",
                    binding: current.binding,
                    value: subst(current.value, gamma.set(current.binding, { kind: "UNKNOWN" })),
                };
            }
            case "NEEDS_CONSTRAINT": {
                return {
                    kind: "NEEDS_CONSTRAINT",
                    binding: current.binding,
                    type: subst(current.type, gamma.set(current.binding, { kind: "UNKNOWN" })),
                };
            }
        }
    };
    return subst(original, gamma);
};
function typesAreEqual(t1, t2, gamma) {
    t1 = getType(t1, gamma);
    t2 = getType(t2, gamma);
    switch (t1.kind) {
        case "UNIT": {
            return t2.kind === "UNIT";
        }
        case "INT": {
            return t2.kind === "INT";
        }
        case "TYPE_VAR": {
            return (t2.kind === "TYPE_VAR"
                && t1.value === t2.value
                && gamma.has(t1.value));
        }
        case "SUM": {
            return (t2.kind === "SUM"
                && t1.value.length === t2.value.length
                && t1.value.every((value, index) => t2.kind === "SUM" &&
                    labelTypesAreEqaul(value, t2.value[index], gamma)));
        }
        case "PRODUCT": {
            return (t2.kind === "PRODUCT"
                && t1.value.length === t2.value.length
                && t1.value.every((value, index) => t2.kind === "PRODUCT" &&
                    labelTypesAreEqaul(value, t2.value[index], gamma)));
        }
        case "ARROW": {
            return (t2.kind === "ARROW"
                && typesAreEqual(t1.value[0], t2.value[0], gamma)
                && typesAreEqual(t1.value[1], t2.value[1], gamma));
        }
        case "REC": {
            return (t2.kind === "REC"
                && t1.binding === t2.binding
                && typesAreEqual(t1.value, t2.value, gamma.set(t1.binding, { kind: "UNKNOWN" })));
        }
        case "NEEDS_CONSTRAINT": {
            return (t2.kind === "NEEDS_CONSTRAINT"
                && t1.binding === t2.binding
                && typesAreEqual(t1.type, t2.type, gamma.set(t1.binding, { kind: "UNKNOWN" })));
        }
    }
}
function labelTypesAreEqaul(lt1, lt2, gamma) {
    return lt1.label === lt2.label && typesAreEqual(lt1.value, lt2.value, gamma);
}
function typecheck(sigma, gamma, e) {
    switch (e.kind) {
        case "ALIAS": {
            return typecheck(sigma, gamma.set(e.ident, getType(e.type, gamma)), e.value);
        }
        case "UNIT": {
            return { kind: "UNIT" };
        }
        case "NUMBER": {
            return { kind: "INT" };
        }
        case "TYPED_IDENT": {
            if (!sigma.has(e.value)) {
                return getType(e.type, gamma);
            }
            else {
                let type = sigma.get(e.value);
                type = getType(type, gamma);
                if (!typesAreEqual(type, e.type, gamma)) {
                    throw new TypeError(`Types dont equal:
						${exports.typeToString(type)}
						${exports.typeToString(e.type)}
					${exports.eToString(e)}
					`);
                }
                return type;
            }
        }
        case "UNTYPED_IDENT": {
            if (!sigma.has(e.value)) {
                throw new TypeError(`Unknown type for variable expression (${exports.eToString(e)})`);
            }
            return getType(sigma.get(e.value), gamma);
        }
        case "LAMBDA": {
            if (sigma.has(e.binding.value)) {
                throw new TypeError(`Cannot shadow variable in expression (${exports.eToString(e)})`);
            }
            if (e.binding.kind === "UNTYPED_IDENT") {
                throw new TypeError(`Lambda parameters must have explicit type (${exports.eToString(e)})`);
            }
            let type = e.binding.type;
            type = getType(e.binding.type, gamma);
            let sigmaprime = sigma.set(e.binding.value, type);
            return {
                kind: "ARROW",
                value: [
                    type,
                    typecheck(sigmaprime, gamma, e.value)
                ]
            };
        }
        case "TYPE_LAMBDA": {
            if (gamma.has(e.binding)) {
                throw new TypeError(`Cannot shadow type variable in expression (${exports.eToString(e)})`);
            }
            let gammaprime = gamma.set(e.binding, { kind: "UNKNOWN" });
            let subtype = typecheck(sigma, gammaprime, e.value);
            subtype = getType(subtype, gamma);
            return {
                kind: "NEEDS_CONSTRAINT",
                binding: e.binding,
                type: subtype,
            };
        }
        case "FIXED": {
            if (sigma.has(e.fn)) {
                throw new TypeError(`Cannot shadow variable ${e.fn} (${exports.eToString(e)})`);
            }
            if (sigma.has(e.binding.value)) {
                throw new TypeError(`Cannot shadow variable ${e.binding.value} (${exports.eToString(e)})`);
            }
            if (e.binding.kind !== "TYPED_IDENT") {
                throw new TypeError(`Fix parameters must have explicit type (${exports.eToString(e)})`);
            }
            let type = { kind: "ARROW", value: [getType(e.binding.type, gamma), getType(e.returnType, gamma)] };
            let actualReturn = typecheck(sigma.set(e.binding.value, getType(e.binding.type, gamma)).set(e.fn, type), gamma, e.value);
            if (!typesAreEqual(e.returnType, actualReturn, gamma)) {
                throw new TypeError(`Recursive function does not match explicit return type (${exports.eToString(e)})`);
            }
            return type;
        }
        case "CALL": {
            let value = typecheck(sigma, gamma, e.value);
            let subst = typecheck(sigma, gamma, e.subst);
            value = getType(value, gamma);
            if (value.kind !== "ARROW") {
                throw new TypeError(`Cannot call a non-function (${exports.eToString(e)})`);
            }
            if (!typesAreEqual(value.value[0], subst, gamma)) {
                throw new TypeError(`Function signature does not match arguments
					${exports.typeToString(value.value[0])}
					${exports.typeToString(subst)}
				(${exports.eToString(e)})`);
            }
            return value.value[1];
        }
        case "TYPE_CALL": {
            let value = typecheck(sigma, gamma, e.value);
            value = getType(value, gamma);
            if (value.kind !== "NEEDS_CONSTRAINT") {
                throw new TypeError(`Cannot constrain non-type function (${exports.eToString(e)})`);
            }
            return typeSubst({ kind: "TYPE_VAR", value: value.binding }, value.type, e.subst, gamma.set(value.binding, { kind: "UNKNOWN" }));
        }
        case "FOLD": {
            let type = getType(e.type, gamma);
            if (type.kind !== "REC") {
                throw new TypeError(`Can only fold into a recursive type (${exports.eToString(e)})`);
            }
            let tauWithSubst = typecheck(sigma, gamma, e.value);
            let tau = typeSubst(e.type, {
                kind: "REC",
                binding: type.binding,
                value: tauWithSubst,
            }, {
                kind: "TYPE_VAR",
                value: type.binding
            }, gamma);
            if (!typesAreEqual(type, tau, gamma)) {
                throw new TypeError(`Cannot fold recursive type. Type does not match
					${exports.typeToString(type.value)}
					${exports.typeToString(tau)}
				(${exports.eToString(e)})`);
            }
            return tau;
        }
        case "UNFOLD": {
            let value = typecheck(sigma, gamma, e.value);
            value = getType(value, gamma);
            if (value.kind !== "REC") {
                throw new TypeError(`Can only unfold a recursive type (${exports.eToString(e)})`);
            }
            // LOOK CLOSELY PLOX
            return typeSubst({
                kind: "TYPE_VAR",
                value: value.binding
            }, value.value, value, gamma.set(value.binding, { kind: "UNKNOWN" }));
        }
        case "TUPLE": {
            let tupleTypes = e.value.map(({ label, value }) => ({ label, value: typecheck(sigma, gamma, value) }));
            return { kind: "PRODUCT", value: tupleTypes };
        }
        case "SUM": {
            let type = getType(e.type, gamma);
            if (type.kind !== "SUM") {
                throw new TypeError(`Cannot use a label with non-sum type (${exports.eToString(e)})`);
            }
            let value = typecheck(sigma, gamma, e.value);
            for (let entry of type.value) {
                if (entry.label === e.sumLabel) {
                    if (typesAreEqual(entry.value, value, gamma)) {
                        return type;
                    }
                    else {
                        throw new TypeError(`Value does not match enclosing type
							${exports.typeToString(entry.value)}
							${exports.typeToString(value)}
						(${exports.eToString(e)})`);
                    }
                }
            }
            throw new TypeError(`Unkown label ${e.sumLabel} (${exports.eToString(e)})`);
        }
        case "EXTRACT": {
            let value = typecheck(sigma, gamma, e.value);
            if (value.kind !== "PRODUCT") {
                throw new TypeError(`Can only extract key from product type (${exports.eToString(e)})`);
            }
            for (let entry of value.value) {
                if (entry.label === e.productLabel) {
                    return entry.value;
                }
            }
            throw new TypeError(`Key does not exist on type (${exports.eToString(e)})`);
        }
        case "CASE": {
            let caseType = typecheck(sigma, gamma, e.binding);
            caseType = getType(caseType, gamma);
            if (caseType.kind !== "SUM") {
                throw new TypeError(`Can only case on sum types (${exports.eToString(e)})`);
            }
            let typeMap = caseType.value.reduce((base, { label, value }) => base.set(label, value), immutable_1.Map());
            let typeSet = immutable_1.Set(typeMap.keys());
            let caseSet = immutable_1.Set();
            let returnType;
            for (let { label, value, binding } of e.value) {
                caseSet = caseSet.add(label);
                if (!typeMap.has(label)) {
                    throw new TypeError(`Casing on label ${label} that does not exist (${exports.eToString(e)})`);
                }
                if (binding.kind === "TYPED_IDENT" && !typesAreEqual(binding.type, typeMap.get(label), gamma)) {
                    throw new TypeError(`Explicit typing does not match inferred type (${exports.eToString(e)})`);
                }
                let sigmaprime = sigma.set(binding.value, typeMap.get(label));
                let valueType = typecheck(sigmaprime, gamma, value);
                if (returnType === undefined) {
                    returnType = valueType;
                }
                else if (!typesAreEqual(valueType, returnType, gamma)) {
                    throw new TypeError(`All branches of case must return the same thing
						${exports.typeToString(valueType)}
						${exports.typeToString(returnType)}
					(${exports.eToString(e)})`);
                }
            }
            if (!typeSet.equals(caseSet)) {
                throw new TypeError(`Missing case in statement (${exports.eToString(e)})`);
            }
            return returnType;
        }
        case "PLUS":
        case "TIMES": {
            let type1 = typecheck(sigma, gamma, e.value[0]);
            type1 = getType(type1, gamma);
            let type2 = typecheck(sigma, gamma, e.value[1]);
            type2 = getType(type2, gamma);
            if (type1.kind !== "INT" || type2.kind !== "INT") {
                throw new TypeError(`Arithmetic operations can only be performed on integers (${exports.eToString(e)})`);
            }
            return { kind: "INT" };
        }
    }
}
function default_1(topLevel) {
    let sigma = immutable_1.Map();
    let gamma = immutable_1.Map();
    return typecheck(sigma, gamma, topLevel);
}
exports.default = default_1;
//# sourceMappingURL=typechecker.js.map
