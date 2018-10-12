from z3 import *

with open("map2.txt", "r") as f:
    cipher, chalbox = eval(f.read())

length, gates, check = chalbox

key = BitVec("key", 128)
s = Solver()

b = [(key >> i) & 1 for i in range(length)]
for name, args in gates:
    if name == "true":
        b.append(1)
    else:
        u1 = b[args[0][0]] ^ args[0][1]
        u2 = b[args[1][0]] ^ args[1][1]
        if name == "or":
            b.append(u1 | u2)
        elif name == "xor":
            b.append(u1 ^ u2)
s.add(b[check[0]] == True ^ check[1])

print(s.check())
print(s.model()[key])

"""
For this challenge, we need to use z3 to solve for a key which will pass the validation.
This is pretty easy since we can just replace the key with symbolic values and constrain the final check at the end
to concretize its value.

$ python decrypt.py 219465169949186335766963147192904921805 map2.txt
Attempting to decrypt map2.txt...
Congrats the flag for map2.txt is: picoCTF{36cc0cc10d273941c34694abdb21580d__aw350m3_ari7hm37ic__}
"""
