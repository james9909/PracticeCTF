# Read bytes and strip header
bytes = open("pico2018-special-logo.bmp", "rb").read()[54:]

dec = ""
for byte in bytes:
    dec += str(ord(byte) & 1)

print(("%x" % int(dec, 2)).decode("hex"))

"""
The goal of the challenge is to read the flag which is encoded in the least significant byte
of each pixel. Since .bmp files encode their pixels directly into the file format as bytes,
this makes it very straightforward when it comes to retrieving the lsb of each byte.
All we need to do is decode the string of lsbs from binary and convert it to ascii in
order to get the flag.

picoCTF{st0r3d_iN_tH3_l345t_s1gn1f1c4nT_b1t5_2903593693}...<extra garbage>
"""
