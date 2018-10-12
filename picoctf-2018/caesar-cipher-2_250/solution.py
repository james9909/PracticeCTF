enc = open("ciphertext", "r").read()

for shift in range(256):
    candidate = ""
    for char in enc:
        candidate += chr(ord(char) + shift % 255)
    if "pico" in candidate:
        print candidate
        break

"""
This is a simple variation on the caesar cipher where the ciphertext was shifted by some amount, but not
just limited to the a-z range. We just need to brute force all the possible shifts to find the flag.

picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}
"""
