from subprocess import Popen, PIPE
import time
import string

guess = [b"0"] * 8
alphabet = string.digits

for i in range(8):
    found = False
    max_time = 0
    value = b"0"
    for char in alphabet:
        char = bytes(char, "utf-8")
        start = time.time()
        guess[i] = char
        out, err = Popen(["./pin_checker"], stdin=PIPE, stdout=PIPE).communicate(b"".join(guess))
        duration = time.time() - start
        if duration > max_time:
            max_time = duration
            value = char
    guess[i] = value
    print(b"".join(guess))

print(b"".join(guess))

"""
$ python3 solution.py
b'90000000'
b'49000000'
b'48900000'
b'48390000'
b'48399000'
b'48390900'
b'48390590'
b'48390519'
b'48390513'
$ nc saturn.picoctf.net 55824
Verifying that you are a human...
Please enter the master PIN code:
48390513
Password correct. Here's your flag:
picoCTF{t1m1ng_4tt4ck_9803bd25}
"""
