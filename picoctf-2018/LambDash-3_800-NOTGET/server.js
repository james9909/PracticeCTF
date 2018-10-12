"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const express = require("express");
const nconf_1 = require("nconf");
const mz_1 = require("mz");
const path = require("path");
const parser = require("body-parser");
const lambda_1 = require("./lambda");
const typechecker_1 = require("./typechecker");
const vm2 = require("vm2");
const nconf = (new nconf_1.Provider())
    .argv()
    .env()
    .defaults({
    PORT: "4001",
    FLAG: "fakeCTF{You didnt think it would be this easy did you? Now go find a real flag}"
});
function start() {
    return __awaiter(this, void 0, void 0, function* () {
        const app = express();
        app.use(parser.urlencoded());
        app.use("/scripts", express.static(path.join(__dirname, "..", "client", "scripts")));
        app.use("/styles", express.static(path.join(__dirname, "..", "client", "styles")));
        app.get("/", (req, res) => __awaiter(this, void 0, void 0, function* () {
            console.log(req.query);
            let { page } = req.query;
            if (page && page.indexOf("..") >= 0) {
                page = undefined;
            }
            page = page || "client/pages/intro.html";
            let fileData = yield mz_1.fs.readFile(path.join(__dirname, "..", "client/index.html"));
            let pageData = yield mz_1.fs.readFile(path.join(__dirname, "..", page));
            let rendered = fileData.toString().replace(/\{server-body\}/g, pageData.toString());
            res.send(rendered);
        }));
        app.post("/run", (req, res) => {
            let code = req.body.code;
            let ast;
            try {
                ast = lambda_1.parse(code);
            }
            catch (e) {
                res.send(`Error -- code did not parse<br>${e.toString()}`);
                return;
            }
            let type;
            try {
                type = typechecker_1.default(ast);
            }
            catch (e) {
                res.send(`Error -- code did not typecheck<br>${e.toString()}`);
                return;
            }
            let vm = new vm2.NodeVM({
                timeout: 1000,
                sandbox: {
                    ast,
                    hidden: {
                        getFlag: ((f) => ((x) => {
                            if (x === "if you can get this you deserve the flag -> abcd1234!@#$%^&*()'") {
                                return f;
                            }
                            return "Bad! " + x;
                        }))(process.env.FLAG)
                    },
                },
                require: {
                    context: "sandbox",
                    external: ["./emulator", "immutable"],
                    root: __dirname,
                },
            });
            try {
                let result = vm.run(new vm2.VMScript(`
				let emulator = require("${__dirname}/emulator");
				module.exports = emulator.resToString(emulator.default(ast));
			`));
                console.log(result);
                res.send(`Result:<br>${result}:${typechecker_1.typeToString(type)}`);
            }
            catch (e) {
                console.log("Wut", e.stack);
                res.send(`Error -- failed to execute<br>${e}`);
            }
        });
        app.listen(nconf.get("PORT"));
    });
}
start();
//# sourceMappingURL=server.js.map
