import string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

enc = "{bvtgvhngm}"

for x in range(1, 26):
    print "%s: %s" % (x, caesar(enc, x))

# Looking through the possible decryptions, we find a readable flag at a shift of 7:
# {icancount}
