from pwntools import *
from RSAwienerHacker import hack_RSA

r = remote("2018shell3.picoctf.com", 59549)

c = int(r.recvline().strip("c: "))
n = int(r.recvline().strip("n: "))
e = int(r.recvline().strip("e: "))
d = hack_RSA(e, n)

print ("%x" % pow(c, d, n)).decode("hex")

"""
We're given a public exponent that is extremely large, which in turn will result in a private exponent that
is much smaller. RSA is vulnerable to Wiener's attack, if d < N^0.25 / 3.

Using a script online, we can calculate d from e and n.
https://github.com/pablocelayes/rsa-wiener-attack

$ python solution.py
picoCTF{w@tch_y0ur_Xp0n3nt$_c@r3fu11y_2026912}
"""
