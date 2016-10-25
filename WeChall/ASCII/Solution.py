ciphertext = "84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 104, 110, 102, 97, 108, 101, 97, 110, 110, 111, 112, 111"

ciphertext = ciphertext.split(", ")
decoded = ""
for char in ciphertext:
    decoded += chr(int(char))

print decoded
