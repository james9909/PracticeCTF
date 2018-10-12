from z3 import *

s = Solver()
x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = BitVecs("x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15", 128)

chars = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15]
for b in chars:
    s.add(b >= 0, b <= 35)

s.add((chars[0] + chars[1]) % 36 == 14,
(chars[2] + chars[3]) % 36 == 24,
(chars[2] - chars[0]) % 36 == 6,
(chars[1] + chars[3] + chars[5]) % 36 == 4,
(chars[2] + chars[4] + chars[6]) % 36 == 13,
(chars[3] + chars[4] + chars[5]) % 36 == 22,
(chars[6] + chars[8] + chars[10]) % 36 == 31,
(chars[1] + chars[4] + chars[7]) % 36 == 7,
(chars[9] + chars[12] + chars[15]) % 36 == 20,
(chars[13] + chars[14] + chars[15]) % 36 == 12,
(chars[8] + chars[9] + chars[10]) % 36 == 27,
(chars[7] + chars[12] + chars[13]) % 36 == 23)

def convert(value):
    """Convert values from the program's ord() to actual characters"""
    if value > 9:
        return chr(value + 55)
    else:
        return chr(value + 48)

print(s.check())
model = s.model()
key = ""
for char in chars:
    key += convert(model[char].as_long())
print(key)

"""
Looking at the assembly, we see that there are various checks throughout the program
that constrain the values of our product key. We can use z3 to easily constrain the values
and come up with a string that will pass these checks. One thing to keep note of is how the
program converts chars to ints, and to constrain appropriately.

One valid product key is "QOWS6OBD37H0DXF0".

picoCTF{c0n5tr41nt_50lv1nG_15_W4y_f45t3r_783243818}
"""
