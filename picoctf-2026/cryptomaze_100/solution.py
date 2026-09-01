import binascii

from Crypto.Cipher import AES

start_state = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]
taps = [63, 61, 60, 58]
lfsr = sum(bit << (63 - i) for i, bit in enumerate(start_state))

bits = []
for i in range(128):
    bit = (lfsr >> 63) & 1
    fb = 0
    for t in taps:
        fb ^= (lfsr >> (63 - t)) & 1
    lfsr = ((lfsr << 1) & 0xFFFFFFFFFFFFFFFF) | fb
    bits.append(bit)

key = bytearray()
for i in range(0, 128, 8):
    key.append(int("".join(map(str, bits[i:i+8])), 2))

enc = binascii.unhexlify("8f0e6d0f5b0dc1db201948b9e0cebd8f4e0f7cb6a86d4243f62f1438e07a632c38338e7e04fbddef0c6260a4eb758417")
flag = ""

cipher = AES.new(key, AES.MODE_ECB)
print(cipher.decrypt(enc))

"""
Do exactly as the problem describes and we can decrypt the flag:

picoCTF{scr8mbledt_flvg_35821959}
"""
