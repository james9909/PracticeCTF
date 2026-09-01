inp = open("digits.bin").read().strip()

dec = bytes()
for i in range(0, len(inp), 8):
    chunk = inp[i:i+8]
    dec += bytes([int(chunk, 2)])

open("out.jpg", "wb").write(dec)

"""
The binary in the file encodes a JPG, which we can see with the header "\xff\xd8" and footer "\xff\xd9".

picoCTF{h1dd3n_1n_th3_b1n4ry_3d2e65ba}
"""
