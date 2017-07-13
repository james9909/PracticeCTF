def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

e = 65537
p = 335445381412686320307419854821396116851
q = 208032399874738495835162222153730872959

enc = open("flag.txt", "r").read()
enc = enc.encode("hex")
enc = int(enc, 16)
tot = (p-1) * (q-1)
n = p * q
d = modinv(e, tot)
print hex(pow(enc, d, n))[2:-1].decode("hex")

"""
The public key used in the RSA encryption is in PEM format, which we can decode with the following command:
$ openssl rsa -pubin -inform PEM -text -noout < key.pub
Public-Key: (256 bit)
Modulus:
    00:9a:48:10:d0:98:b1:cb:ff:75:68:2a:0a:9d:da:
    84:31:51:97:eb:4d:aa:58:18:62:56:27:4c:03:61:
    dc:e6:0d
Exponent: 65537 (0x10001)

From this, we get the hex-encoded modulus:
009a4810d098b1cbff75682a0a9dda84315197eb4daa58186256274c0361dce60d

In decimal, that's
69783507722178132619820485783352049428969858299739616863075072996637000132109

We can look up the factors of the modulus with factordb, and we get that the two factors are
208032399874738495835162222153730872959 and 335445381412686320307419854821396116851.

Finally, now that we know p, q, and e, we have all we need to decrypt the flag

$ python solution.py
flag{bad_primes_are_best_primes}
"""
