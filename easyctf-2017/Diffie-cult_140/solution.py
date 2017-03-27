import operator

# g^a mod p = 421049228295820
# g^b mod p = 105262307073955
# p=442101689710611

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def prime_factors(n):
    i = 2
    factors = set()
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

# Known
A = 421049228295820
B = 105262307073955
p = 442101689710611
factors = sorted(prime_factors(p))
print factors

g = reduce(operator.mul, factors[2:])
print "g: %d" % g

a = 0
while pow(g, a, p) != A:
    a += 1
print "a: %d" % a

b = 0
while pow(g, b, p) != B:
    b += 1
print "b: %d" % b

shared_secret = pow(B, a, p)
assert shared_secret == pow(A, b, p)

print "Shared secret: %d" % shared_secret

# 421049228295820
