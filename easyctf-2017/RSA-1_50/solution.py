p = 34022950344780880819596863068064899352464257267712477930082091619184075807627771
q = 31796716812991406801082958039733300284584247538511358592044388937758777985150713
e = 65537
c =                                                                                                                                           921533063644229686659547618611357168149642723583754500761295258788367941439319606984331553819560676246833302184873968993660092023754025960702262728724802088007

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

# easyctf{wh3n_y0u_h4ve_p&q_RSA_iz_ez_0ec66d17}
