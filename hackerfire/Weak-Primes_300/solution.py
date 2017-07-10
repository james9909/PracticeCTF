def decrypt_RSA(privkey, message):
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    from base64 import b64decode
    key = open(privkey, "r").read()
    rsakey = RSA.importKey(key)
    decrypted = rsakey.decrypt(message)
    return decrypted

enc = open("flag.txt", "r").read()
dec = decrypt_RSA('priv.key', enc)

print dec

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

Using rsatool, we can generate the private key with the following command:
$ python rsatool.py -p 208032399874738495835162222153730872959 -q 335445381412686320307419854821396116851 -o priv.key

Finally, we have all we need to decrypt the flag

$ python solution.py
flag{bad_primes_are_best_primes}
"""
