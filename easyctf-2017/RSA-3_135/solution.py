import math

n = 0x27335d21ca51432fa000ddf9e81f630314a0ef2e35d81a839584c5a7356b94934630ebfc2ef9c55b111e8c373f2db66ca3be0c0818b1d4eda7d53c1bd0067f66a12897099b5e322d85a8da45b72b828813af23
e = 0x10001
c = 0x9b9c138e0d473b6e6cf44acfa3becb358b91d0ba9bfb37bf11effcebf9e0fe4a86439e8217819c273ea5c1c5acfd70147533aa550aa70f2e07cc98be1a1b0ea36c0738d1c994c50b1bd633e3873fc0cb377e7

p = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780869
q = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780871

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

t = (p-1) * (q-1)
d = modinv(e, t)
dec = pow(c, d, n)
print hex(dec)[2:-1].decode("hex")

# easyctf{tw0_v3ry_merrry_tw1n_pr1m35!!_417c0d}
