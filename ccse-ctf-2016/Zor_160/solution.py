plaintext = "Hello World!!"
ciphertext = "333f033e3078381d2d3654535c".decode("hex")

key = ""

for x in range(len(plaintext)):
    key += chr(ord(ciphertext[x]) ^ ord(plaintext[x]))

print key

# {ZoR_Xor_Z0r}
