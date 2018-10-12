from pwn import *
import string

def chunks(s, n):
    ret = []
    for x in range(0, len(s), n):
        ret.append(s[x:x+n])
    return ret

def encrypt(payload):
    print(payload)
    r = remote("2018shell3.picoctf.com", 33893, level="error")
    r.recv()
    r.recv()
    r.sendline(payload)
    ciphertext = r.recvline().strip()
    r.close()
    return ciphertext

flag = ""
cpt = bytearray("A"*27 + "ifying code is: ")
charset = string.ascii_letters + string.digits + string.punctuation
i = 0
while True:
    cpt = cpt[1:]
    found = False
    for char in charset:
        blocks = (chunks(encrypt(cpt + flag + char + "A"*(64-i)), 32))
        guess = blocks[5]
        if blocks.count(guess) > 1:
            found = True
            flag += char
            print(flag)
            break
    print(cpt)
    if not found:
        print("Rip")
        break
    i += 1

"""
The vulnerability here lies in ECB mode which encrypted each block of the plaintext into
a deterministic block of ciphertext. The issue with ECB is that blocks containing the same plaintext
will encrypt to the same ciphertext, meaning that we can brute force the flag byte by byte
and check to see if there are duplicate ciphertext blocks. The traditional method of aligning the end of the flag
to the end of a block won't work since a new line comes after the flag, but we can instead align
the start of the flag to the start of a block and brute force from left to right.

picoCTF{@g3nt6_1$_th3_c00l3$t_9121600}
"""
