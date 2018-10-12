enc = "\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x50\x14\x5d\x00\x19\x17\x59\x52\x5d"
key = "You have now entered the Duck Web"
dec = ""
for x in range(len(enc)):
    dec += chr(ord(enc[x]) ^ ord(key[x]))

print(dec)

"""
Browsing the disassembly, we see that our input is being xor'd with the string "You have now entered..."
and it's being compared to a secret buffer. Because of the properties of xor, we can reverse this operation
to decrypt the flag.

picoCTF{qu4ckm3_5f8d9c17}
"""
