"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.toString = Symbol("toString");
function getCleanObject() {
    let obj = {};
    for (let prop of Object.getOwnPropertyNames(obj.__proto__)) {
        obj[prop] = undefined;
    }
    obj.__proto__ = undefined;
    return obj;
}
function emulate(e, sigma) {
    switch (e.kind) {
        case "ALIAS": {
            return emulate(e.value, sigma);
        }
        case "UNIT": {
            return null;
        }
        case "NUMBER": {
            return e.value;
        }
        case "TYPED_IDENT":
        case "UNTYPED_IDENT": {
            return sigma[e.value];
        }
        case "LAMBDA": {
            let lambda = function (param) {
                return emulate(e.value, Object.assign({}, sigma, { [e.binding.value]: param }));
            };
            lambda[exports.toString] = () => "[lambda]";
            return lambda;
        }
        case "TYPE_LAMBDA": {
            let lambda = function () {
                return emulate(e.value, sigma);
            };
            lambda[exports.toString] = () => "[type_lambda]";
            return lambda;
        }
        case "FIXED": {
            let f = function (param) {
                return emulate(e.value, Object.assign({}, sigma, { [e.binding.value]: param, [e.fn]: f }));
            };
            f[exports.toString] = () => "[fix]";
            return f;
        }
        case "CALL": {
            let arg = emulate(e.subst, sigma);
            let fn = emulate(e.value, sigma);
            return fn(arg);
        }
        case "TYPE_CALL": {
            let fn = emulate(e.value, sigma);
            return fn();
        }
        case "FOLD": {
            return emulate(e.value, sigma);
        }
        case "UNFOLD": {
            return emulate(e.value, sigma);
        }
        case "TUPLE": {
            let obj = getCleanObject();
            for (let i = 0; i < e.value.length; i++) {
                let { label, value } = e.value[i];
                obj[label] = emulate(value, sigma);
            }
            obj[exports.toString] = () => "{ tuple }";
            return obj;
        }
        case "SUM": {
            let obj = getCleanObject();
            obj[e.sumLabel] = emulate(e.value, sigma);
            obj[exports.toString] = () => "< sum >";
            return obj;
        }
        case "EXTRACT": {
            let value = emulate(e.value, sigma);
            return value[e.productLabel];
        }
        case "CASE": {
            let binding = emulate(e.binding, sigma);
            for (let entry of e.value) {
                if (binding[entry.label] !== undefined) {
                    let substVal = binding[entry.label];
                    return emulate(entry.value, Object.assign({}, sigma, { [entry.binding.value]: substVal }));
                }
            }
            throw new Error(`Failed to find case ${Object.keys(binding)}`);
        }
        case "PLUS": {
            let e1 = emulate(e.value[0], sigma);
            let e2 = emulate(e.value[1], sigma);
            return e1 + e2;
        }
        case "TIMES": {
            let e1 = emulate(e.value[0], sigma);
            let e2 = emulate(e.value[1], sigma);
            return e1 * e2;
        }
    }
}
function resToString(r) {
    if (typeof r === "object" || typeof r === "function") {
        return r[exports.toString]();
    }
    else {
        return r.toString();
    }
}
exports.resToString = resToString;
function emulator(e) {
    return emulate(e, getCleanObject());
}
exports.default = emulator;
//# sourceMappingURL=emulator.js.map
