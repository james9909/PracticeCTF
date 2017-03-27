n = 76404616482339779852243185646376798277397
e = 65537
c = 27878102603436665559732144498092566559591

p = 201504694364335021223
q = 379170404557398163939

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

n = p * q
t = (p-1) * (q-1)
d = modinv(e, t)
dec = pow(c, d, n)
print hex(dec)[2:-1].decode("hex")

# We aren't given p and q, but we are given a relatively small n
# Because of this, we can look up its factors online (http://factordb.com)
# Knowing p and q, the problem becomes the same as RSA 1

# flag{l0w_n_adfe}
