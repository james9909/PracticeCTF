alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}"
enc = "00 30 20 50 40 70 60 90 80 B0 A0 D0 C0 F0 E0 11 01 31 21 51 41 71 61 91 81 B1 02 32 22 52 42 72 62 92 82 B2 A2 D2 C2 F2 E2 13 03 33 23 53 43 73 63 93 83 B3 15 05 35 25 55 45 75 65 95 85 E3 A1 C1".split(" ")

mappings = {}
for x in range(len(alphabet)):
    mappings[enc[x]] = alphabet[x]

flag = ""
desired = "11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 45 20 35 05 70 20 95 50 C1".split(" ")
for char in desired:
    flag += mappings[char]
print(flag)

"""
Playing around with the encryption, we see that the encryption is deterministic based on the character,
no matter where it is in the plaintext. Knowing this, we can just build a map of all the plaintext
characters and their corresponding outputs to decode the flag.

picoCTF{qu4ckm3_5c21fc8d}
"""
