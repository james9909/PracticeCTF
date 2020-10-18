n = 99157116611790833573985267443453374677300242114595736901854871276546481648883
g = 99157116611790833573985267443453374677300242114595736901854871276546481648884
c = 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869

def L(x):
    return (x - 1) / n

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

def lcm(x, y):
    g, _, _ = egcd(x, y)
    return (x * y) // g

p = 310013024566643256138761337388255591613
q = 319848228152346890121384041219876391791
lmbda = lcm(p - 1, q - 1)
mu = modinv(L(pow(g, lmbda, n*n)), n)
m = (L(pow(c, lmbda, n*n)) * mu) % n
print(("%x" % m).decode("hex"))

"""
The description of the problem suggests that the given information is related to the Pailier cryptosystem, which is a
public key cryptosystem. The key generation scheme is described here: https://en.wikipedia.org/wiki/Paillier_cryptosystem

All we need are the factors of p and q, then we can replicate the decryption scheme to get the flag.
Fortunately, the factors are available on factordb, making this problem fairly simple.

actf{crypto_lives}
"""
