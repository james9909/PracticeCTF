import hashlib
import string

hashes = open("hexstrings.txt", "r").read().split("\n")

lookup = {}
CHARSET = string.printable
for char in CHARSET:
    lookup[hashlib.md5(char).hexdigest()] = char

dec = ""
for h in hashes:
    dec += lookup.get(h, "")

print dec

# Each line in the file is an MD5 hash of a single character
# Knowing this, we can generate a lookup table containing letters and their respective MD5 hashes to decrypt the ciphertext

# Im far too lazy to put anything meaningful here. Instead, here's some information about what you just solved.
# The MD5 algorithm is a widely used hash function producing a 128-bit hash value. Although MD5 was initially designed to be used as a cryptographic hash function, it has been found to suffer from extensive vulnerabilities. It can still be used as a checksum to verify data integrity, but only against unintentional corruption.
# Like most hash functions, MD5 is neither encryption nor encoding. It can be cracked by brute-force attack and suffers from extensive vulnerabilities as detailed in the security section below.
# MD5 was designed by Ronald Rivest in 1991 to replace an earlier hash function MD4.[3] The source code in RFC 1321 contains a "by attribution" RSA license. The abbreviation "MD" stands for "Message Digest."
# The security of the MD5 has been severely compromised, with its weaknesses having been exploited in the field, most infamously by the Flame malware in 2012. The CMU Software Engineering Institute considers MD5 essentially "cryptographically broken and unsuitable for further use".[4]
# easyctf{1_h0p3_y0u_d1dn7_d0_7h47_by_h4nd}
