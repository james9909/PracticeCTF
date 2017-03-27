import string

alphabet = string.ascii_lowercase

def caesar(plaintext, shift):
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

enc = "rnflpgs{lbhtbgvg}"
for x in range(1, 26):
    candidate = caesar(enc, x)
    if "easyctf" in candidate:
        print candidate
        break

# easyctf{yougotit}
