from Crypto.Util.number import GCD, isPrime

def primegen():
    """
    Generates primes lazily via the sieve of Eratosthenes
    Input: none
    Output:
        Sequence of integers
    Examples:
    >>> list(takewhile(lambda x: x < 100, primegen()))
    [2, 3, 5, 7, 11, 13, 8, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    yield 2; yield 3; yield 5; yield 7; yield 11; yield 13
    ps = primegen() # yay recursion
    p = next(ps) and next(ps)
    q, sieve, n = p**2, {}, 13
    while True:
        if n not in sieve:
            if n < q: yield n
            else:
                _next, step = q + 2*p, 2*p
                while _next in sieve: _next += step
                sieve[_next] = step
                p = next(ps)
                q = p**2
        else:
            step = sieve.pop(n)
            _next = n + step
            while _next in sieve: _next += step
            sieve[_next] = step
        n += 2

def pollard_rho(N, f=None):
    """
    Pollard's rho algorithm can fail for some inputs.
    Simply change the f or seed values if it fails.
    """
    x, y, d = 2, 2, 1
    if f == None :
        f = lambda x: (x*x+1) % N
    tmp = []
    while d <= 1:
        x = f(x)
        if not x in tmp :
            tmp.append(x)
        else:
            break
        y = f(f(y))
        d = GCD(x - y, N)
        if d != 1 :
            if 1 < d < N : return d
            if d == N : return None
    return d

def pollard_pm1(N):
    """
    For one of N's prime p,
        1. If (p-1) is a K-smooth number. (k is small)
        2. When all (p-1)'s factor were iterated by b
    Then it can be factorization by pollard_pm1.
    ** It may failed if the degree of (p-1)'s factors is greater than 1. **
    """
    if isPrime(N):
        return N
    a = 2
    primes = primegen()
    for b in primes :
        try :
            a = pow(a, b, N)
            p = GCD(a - 1, N)
            if 1 < p < N:
                return p
        except :
            print("Pollard P-1 Failed.")
            return 0

def pollard_brute(N):
    """
    For one of N's prime p,
        1. If (p-1) is a K-smooth number. (k is small)
        2. When all (p-1)'s factor were iterated by b
    Then it can be factorization by pollard_pm1.
    """
    a = 2
    b = 1
    factors = []
    if isPrime(N) : return N
    try :
        while True:
            a = pow(a, b, N)
            p = GCD(a - 1, N)
            if 1 < p < N:
                factors.append(p)
                print(f"factor found: {p}")
                q = N // p
                if isPrime(q) :
                    print(f"factor found: {q}")
                    factors.append(q)
                    return factors
            b += 1
    except:
        return factors

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

e = 0x10001
n = int('65446ab139efe9744c78a271ad04d94ce541a299f9d4dcb658f66f49414fb913d8ac6c90dacc1ad43135454c3c5ac76c56d71d2816dac23db5c8caa773ae2397bd5909a1f2823c230f44ac684c437f16e4ca75d50b75d2f7e5549c034aa8a723c9eaa904572a8c5c6c1ed7093a0695522a5c41575c4dbf1158ca940c02b223f50ae86e6782819278d989200a2cd2be4b7b303dffd07209752ee5a3060c6d910a108444c7a769d003bf8976617b4459fdc15a2a73fc661564267f55be6a0d0d2ec4c06a4951df5a096b079d9e300f7ad72fa6c73a630f9a38e472563434c10225bde7d08c651bdd23fd471077d44c6aab4e01323ed78641983b29633ad104f3fd', 16)
c = int('19a98df2bfd703a31fedff8a02d43bc11f1fb3c15cfa7a55b6a32b3532e1ac477f6accc448f9b7d2b4deaae887450217bb70298afaa0f5e31a77e7c6f8ba1986979f15d299230119e3dd7e42eb9ca4d58d084d18b328fbe08c8909a2afc67866d6550e4e6fa27dc13d05c51cc87259fe73e2a1890cc2825d76c8b2a99f72f6023fc96658ac355487a6c275717ca6c13551094818efae1cec3c8773cc5a72fed518c00a53ba9799d9d5c182795dfcece07c727183fdd86fd2cb4b95e9f231be1858320aa7f8430885eb3d24300552d1a83158636316e55e6ac0a30a608964dbf2c412aed6a15df5fd49e737f7c06c02360d0c292abc33a3735152db2fb5bc5f6d', 16)

p, q = pollard_brute(n)
print(p, q)
totient = (p-1) * (q-1)
d = modinv(e, totient)

plaintext = pow(c, d, n)
print(plaintext)
print(bytes.fromhex(hex(plaintext)[2:]))

"""
The generated primes are smooth, so we can use Pollard's algorithm to find the factors of n. Once we have the factors of n, decoding the ciphertext becomes trivial.

picoCTF{376ebfe7}
"""
