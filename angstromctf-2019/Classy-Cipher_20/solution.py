enc = ":<M?TLH8<A:KFBG@V"
offset = ord("a") - ord(enc[0])

dec = ""
for char in enc:
    dec += chr(ord(char) + offset)
print(dec)

"""
This is a classic caesar cipher, except over the entire set of ascii characters, not just the alphabet.
We know that the flag starts with "actf", so we can determine the shift used pretty easily.
The rest of the work comes down to undoing the shift to get the flag.

actf{so_charming}
"""
