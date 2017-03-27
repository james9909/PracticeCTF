from pwn import remote

HOST = "paillier.tcp.easyctf.com"
PORT = 8570

def encrypt(m, r=1):
    conn = remote(HOST, PORT)
    conn.recv(1024)
    conn.sendline(str(m))
    conn.recv(1024)
    conn.sendline(str(r))
    ret = int(conn.recv(1024).split(" ")[1])
    conn.close()
    return ret

n = encrypt(1, 1) - 1
print "n: %s" % n

flag = "easyctf{3ncrypt_m3!}"
flag = int(flag.encode("hex"), 16)
print "flag: %s" % flag

# Factors of the flag
factors = [3, 5, 191, 233, 661, 16273, 127037, 44028143914423, 14411336288343667]
encrypted = pow(encrypt(factors[0]), factors[1], n**2)
for factor in factors[2:]:
    encrypted = pow(encrypted, factor, n**2)

print encrypted

# Looking at the Paillier cryptosystem, we find that it is homomorphic, which is defined as
# "a form of encryption that allows computations to be carried out on ciphertext,
# thus generating an encrypted result which, when decrypted, matches the result of operations performed on the plaintext."

# The specific property we are interested in is the following:
# E(m1, r2)^m2 % n^2 = E(m1*m2 % n)

# We can calculate n by encrypting with m=1 and r=1, then subtracting by 1.
# Using the factors of the flag, we can generate the full encrypted version of the flag:

# Steps:
# E(3)^5 % n^2 = E(15)
# E(15)^191 % n^2 = E(2865)
# E(2865)^233 % n^2 = E(667545)
# E(667545)^661 % n^2 = E(441247245)
# E(441247245)^16273 % n^2 = E(7180416417885)
# E(7180416417885)^127037 % n^2 = E(912178560478856745)
# ...

# Finally, we get that the full, encrypted version of "easyctf{3ncrypt_m3!}" is:
# 44073117240618665780675193850837939995438219250244678211539041436428154743261238082817577099306521708734123381615432054274681465095612422847370622010652215512660940106734460138798004151939831278940754163448609294265458598883535128433424615303280599380544523443593952238464672302887846705279608801286723167548136016323776193330983364067235836166569465230366
