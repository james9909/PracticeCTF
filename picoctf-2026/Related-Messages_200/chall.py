from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

Message = bytes_to_long(b"[redacted]")
Message_fixed = bytes_to_long(b"[redacted]")
e = 0x11
p = getPrime(1024)
q = getPrime(1024)
phi = (p-1) * (q-1)
d = inverse(e, phi)
N = p*q

ciphertext = pow(Message, e, N)
ciphertext2 = pow(Message_fixed, e, N)

print(ciphertext, ciphertext2)
print(Message - Message_fixed)
print(N)
