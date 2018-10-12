from pwn import *

r = remote("2018shell3.picoctf.com", 42185)
print(r.recv().strip())
print(r.recv().strip())
r.sendline("i")
print(r.recvline().strip());
print(r.recvline().strip());
filename = r.recvline().strip()
print(filename)
filename = filename.strip(".txt").replace("_", "^")

print(r.recv())
r.sendline("n")
print(r.recv())
print(r.recv())
r.sendline(filename)
print(r.recv())
r.sendline("y")
print(r.recv())
print(r.recvline().strip())
code = r.recvline().strip()
print(code)
print(r.recv())

code = code.decode("base64")
for x in range(len(code)):
    r.sendline("e")
    new_code = code[:x] + chr(ord(code[x]) ^ 1) + code[x+1:]
    r.sendline(new_code.encode("base64"))
    resp = r.recvline()
    if "picoCTF" in resp:
        print(resp)
        break
    print(r.recvline().strip())

"""
The vulnerability in this challenge lies with the fact that AES counter mode is being used.
Although the counter is randomized per run, it's never incremented or changed. Because of this,
any files that we encrypt with the same filename will produce the same share code.
The tricky part is being able to encrypt the flag filename, since the program won't allow us to
encrypt any files with an underscore. We can bypass this by encrypting a similar filename with the underscore
replaced and brute forcing a bit flip.

picoCTF{alw4ys_4lways_Always_check_int3grity_6ce3f91c}
"""
