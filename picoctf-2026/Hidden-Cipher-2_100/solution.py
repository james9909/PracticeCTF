from pwn import *

def decode(enc, key):
    flag = ""
    for char in enc:
        flag += chr(char // key)
    return flag

r = remote("crystal-peak.picoctf.net", 59412)
prompt = r.recvuntil("?")
print(prompt)
ans = int(eval(prompt.decode().replace("What is", "")[:-1]))
print(ans)
r.sendline(str(ans).encode())
print(r.recvline())
encoded = r.recvline().strip()
encoded = list(map(int, encoded.decode().split(", ")))
print(decode(encoded, ans))

"""
Reversing the binary, we see that the program generates a random math prompt and encodes the flag
by multiplying each character by the answer to the math problem.

Since we're given the prompt, we can dynamically evaluate it for the key which makes decoding the output very
straightforward.

> python3 solution.py
[+] Opening connection to crystal-peak.picoctf.net on port 59412: Done
/home/james/Dev/PracticeCTF/picoctf-2026/Hidden-Cipher-2_100/solution.py:10: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  prompt = r.recvuntil("?")
b'What is 2 + 5?'
7
b' Encoded flag values:\n'
picoCTF{m4th_b3h1nd_c1ph3r_1bee6cef}
"""
