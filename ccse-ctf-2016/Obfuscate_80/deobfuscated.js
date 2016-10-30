function packed(p, a, c, k, e, d) {
    e = function(c) {
        return c.toString(36)
    };
    if (true) {
        while (c--) {
            d[c.toString(a)] = k[c] || c.toString(a)
        }
        k = [function(e) {
            return d[e]
        }];
        e = function() {
            return '\\w+'
        };
        c = 1
    };
    while (c--) {
        if (k[c]) {
            p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c])
        }
    }
    return p
}
var p = '1 2=["\\8\\9\\7\\b\\6\\4\\3\\5\\a\\i\\c\\j\\h\\g\\d\\e"];1 f=2[0];';
var a = 20;
var c = 20;
var k = '|var|_0x2785|x50|x7D|x51|x2A|x62|x67|x39|x63|x2B|x6F|x45|x70|password|x66|x56|x58|x42'.split('|');
var e = 0;
var d = {};

eval(packed(p, a, c, k, e, d));

// var _0x2785=["\\x67\\x39\\x62\\x2B\\x2A\\x7D\\x50\\x51\\x63\\x58\\x6F\\x42\\x56\\x66\\x45\\x70"];
// var password=_0x2785[0];

console.log(password);

// The password is g9b+*}PQcXoBVfEp. Enter it in to get the flag:
// {0bfuscat1on<de0bfuscat1on}
