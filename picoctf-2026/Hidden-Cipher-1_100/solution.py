import binascii
flag = binascii.unhexlify("235a201d702015483b1d412b265d3313501f0c072d135f0d2002302d01156a57224306172e")

key = [0x53, 0x33, 0x43, 0x72, 0x33, 0x74]

dec = ""
for i, char in enumerate(flag):
    dec += chr((key[i % 6]) ^ char)

print(dec)

"""
The first thing we notice about the binary is that it's packed using `upx`. Luckily decoding the binary can be done by running `upx -d hiddencipher`.

Disassembling the given program we see that the cipher involves xoring each character in the flag with a hard-coded key, in this case '\x53\x33\x43\x72\x33\x74' and then printed out as hex. All we need to do is xor each character in the encrypted flag with the key to decode it.

> nc candy-mountain.picoctf.net 58978
Here your encrypted flag:
235a201d702015483b1d412b265d3313501f0c072d135f0d2002302d01156a57224306172e
> python3 solution.py
picoCTF{xor_unpack_4nalys1s_2a9da15c}
"""
