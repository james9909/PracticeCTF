from pwn import *

def stage_1(s):
    return "{:x}".format(int(s, 2)).decode("hex")

def stage_2(s):
    return "".join(chr(int(x, 8)) for x in s)

def stage_3(s):
    return s.decode("hex")

r = remote("2019shell1.picoctf.com", 7380)
print(r.recvline())
print(r.recvline())

### Stage 1: Decode binary string
prompt = r.recvline()
print(prompt)
binary = prompt.split(" ")[3:-3]
print(r.recvline())
print(r.recvline())
print(r.recvline())
r.sendline(stage_1("".join(binary)))
print(r.recvline())

### Stage 2: Decode octal string
prompt = r.recvline()
print(prompt)
octal = prompt.split(" ")[5:-3]
print(r.recvline())
r.sendline(stage_2(octal))

### Stage 3: Hexadecimal
prompt = r.recvline()
print(prompt)
octal = prompt.split(" ")[4]
print(r.recvline())
r.sendline(stage_3(octal))
print(r.recvline())
print(r.recvline())

"""
This problem requires converting 3 different bases: 2, 8, and 16.
Passing all 3 prompts will give us the flag:

picoCTF{learning_about_converting_values_819ada06}
"""
