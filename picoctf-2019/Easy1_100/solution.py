enc = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

dec = ""
for c, k in zip(enc, key):
    base = ord(k) - ord("A")
    shifted = ord(c) - ord("A")
    diff = shifted - base
    if diff < 0:
        diff += 26
    dec += chr(diff + ord("A"))

print(dec)

"""
This can be manually solved by looking through each pair of encrypted and key chars, and
using the lookup table given in the problem (row is the key and the encrypted character locates the column).

Alternatively, looking at the table, we can see a pattern where each row in the table
shifts the alphabet to the right by 1, similar to a caesar cipher.

Regardless of the method, we get the flag: picoCTF{CRYPTOISFUN}
"""
