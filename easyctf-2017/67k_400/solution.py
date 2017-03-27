import re
import string
import subprocess

def run(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = process.stdout.read()
    return output

def group(string, n):
    return [string[x:x+n] for x in range(0, len(string), n)]

class Analyzer():

    def __init__(self, binary):
        self.binary = binary
        self.first_num_addr = ""
        self.second_num_addr = ""
        self.function_call_addr = ""

    def get_line(self, address):
        index = self.asm.find(address + ":")
        if index == -1:
            return ""
        temp = self.asm[index:]
        return temp[:temp.find("\n")]

    def get_instruction(self, address):
        line = self.get_line(address)
        instruction = line.split("\t")[-1]
        operation = ""
        operands = ""
        while instruction[0] in string.ascii_letters:
            operation += instruction[0]
            instruction = instruction[1:]
        operands = instruction.strip()
        return operation, operands

    def get_data(self, address):
        line = self.get_line(address)
        data = line.split("\t")[1]
        bits = data.split(" ")[::-1]
        return "".join(bits)

    def get_function(self):
        function_addr = self.get_instruction(self.function_call_addr)[1][2:]
        instruction = self.get_instruction(function_addr)[0]
        if instruction == "sub":
            function = lambda x, y: x-y
        elif instruction == "add":
            function = lambda x, y: x+y
        elif instruction == "xor":
            function = lambda x, y: x^y
        else:
            raise Exception("unexpected instruction found: %s" % instruction)
        return function

    def get_section_name(self, instruction):
        index = self.asm.find(instruction)
        if index == -1:
            if ":" in instruction:
                # Hack, if an address was passed in
                addr = int(instruction[:-1], 16)
                while index == -1:
                    addr -= 1
                    index = self.asm.find(hex(addr)[2:] + ":")
            else:
                raise Exception("could not find section name")
        temp = self.asm[:index]
        index = temp.rfind("<")
        temp = temp[index:]
        section = temp[1:temp.find(">")]
        return section

    def get_section(self, section_name):
        section = run("objdump -s -j %s %s" % (section_name, self.binary))
        section = "\n".join(section.split("\n")[4:])
        start = int(section[1:7], 16)
        section = section.split("\n")
        new_section = ""
        for line in section:
            line = line.strip()[7:]
            line = line.split(" ")[:5]
            new_section += "".join(line)
        return start, new_section

    def disassmble_section(self, section_name):
        section = run("objdump -D -j %s %s" % (section_name, self.binary))
        section = "\n".join(section.split("\n")[7:])
        return section

    def get_first_num(self):
        instruction = self.get_instruction(self.first_num_addr)
        address = instruction[1].split(",")[0][2:]
        section_name = self.get_section_name(address + ":")
        start, section = self.get_section(section_name)
        address = int(str(address), 16)
        index = 0
        while index < address-start:
            index += 1
            section = section[1:]
        num = section[index:index+8]
        num = int("".join(group(num, 2)[::-1]), 16)
        return num

    def get_second_num(self):
        instruction = self.get_instruction(self.second_num_addr)
        num = instruction[1].split(",")[0]
        return int(num[3:], 16)

    def set_addresses(self):
        section = self.disassmble_section(self.get_section_name("call   *0x4")).split("\n")
        i = 0
        num_calls = 0
        while i < len(section):
            line = section[i]
            if "call" in line:
                num_calls += 1
            if num_calls == 3:
                self.function_call_addr = line[2:8]
                self.first_num_addr = section[i-2][2:8]
                self.second_num_addr = section[i-1][2:8]
                return
            i += 1
        raise Exception("could not set addresses")

    def analyze(self):
        print "[*] Analyzing %s..." % self.binary
        asm = run("objdump -D %s" % self.binary)
        self.asm = asm
        self.set_addresses()
        function = self.get_function()
        n1 = int(self.get_first_num())
        n2 = int(self.get_second_num())
        result = function(n1, n2)
        self.input = result
        print "[*] Input found: %s" % self.input

    def run(self):
        output = run("echo %s | ./%s" % (self.input, self.binary))
        answer = re.search("\((.*)\)", output)
        if answer:
            print "[*] Correct!"
            return answer.group(1)
        raise Exception("Incorrect input.")

dec = ""
for x in range(67139):
    binary = hex(x)[2:].zfill(5) + ".exe"
    a = Analyzer("binaries/%s" % binary)
    try:
        a.analyze()
    except Exception, e:
        print e
        break

    dec += a.run()

open("script.js", "a").write(dec)

"""
After failing to use angr to solve the problem, I decided to solve each binary by analyzing the disassembly
Luckily, each executable follows the same format:

read number
result = f(n1, n2) where f is either xor, add, or subtract
if number == result
    print output
else
    print insult

From the disassembly, we can get the numbers n1 and n2, and f()

Example:
$ objdump -D binaries/0002e.exe
...
402022:       a1 38 30 40 00          mov    0x403038,%eax
402027:       b9 ec 72 9f b6          mov    $0xb69f72ec,%ecx
40202c:       e8 33 00 00 00          call   0x402064
402031:       3b 05 18 30 40 00       cmp    0x403018,%eax
...
402064:       31 c8                   xor    %ecx,%eax
402066:       c3                      ret
...

From here, we know that the first number is taken from address 0x403038, and that the second number is
0xb69f72ec, or 3063902956. We also know that we need to xor the two numbers together to get the correct input

Combine all the correct inputs to get a javascript program
The script takes a while because it runs each binary separately to validate that the inputs are correct, but it could
be made faster if the actual decryption itself was reversed

$ python solution.py
wait for a long time
$ node script.js
undefined:2
alert("The flag is easyctf{double_you_tee_eff?so_mAny_b1ns}");
^

ReferenceError: alert is not defined
    at eval (eval at <anonymous> (/home/james/Dev/CTF/easyctf-2017/67k_400-INCOMPLETE/script.js:1:902), <anonymous>:2:1)
    at Object.<anonymous> (/home/james/Dev/CTF/easyctf-2017/67k_400-INCOMPLETE/script.js:1:67200)
    at Module._compile (module.js:541:32)
    at Object.Module._extensions..js (module.js:550:10)
    at Module.load (module.js:458:32)
    at tryModuleLoad (module.js:417:12)
    at Function.Module._load (module.js:409:3)
    at Module.runMain (module.js:575:10)
    at run (bootstrap_node.js:352:7)
    at startup (bootstrap_node.js:144:9)

This was meant to be run in a browser, but we get the flag anyways:
easyctf{double_you_tee_eff?so_mAny_b1ns}
"""
