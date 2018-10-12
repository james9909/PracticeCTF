def egcd(a,b): # Extended Euclidean Algorithm
    if a == 0:
        return (b,0,1);
    else:
        g,y,x = egcd(b%a,a);
        return (g, x - (b // a) * y, y);

def modinv(a,m): # Modular Inverse Finder
    g, x, y = egcd(a,m);
    if g != 1:
        raise Exception('modular inverse does not exist');
    else:
        return x % m;
c = 8342235315696612857318085265505351481067427501588041685421287778577778620832584
n = 13389630707382530919395268938531526108775554274009669337031991438038596377077653
e = 65537

# Calculated from https://www.alpertron.com.ar/ECM.HTM
p = 142310688780222542324193797616227148181
q = 94087315732557531013272283071652137037313
assert p * q == n
tot = (p-1) * (q-1)

d = modinv(e, tot)
print(("%x" % pow(c, d, n)).decode("hex"))

"""
The first thing to notice is that the given N values are very small. Knowing this, we can attempt to
factor it for p and q. Using a site like https://www.alpertron.com.ar/ECM.HTM allows us to
retrieve the prime factors relatively quickly, which we can then use to decrypt the ciphertext
as usual.

picoCTF{us3_l@rg3r_pr1m3$_4117}
"""
