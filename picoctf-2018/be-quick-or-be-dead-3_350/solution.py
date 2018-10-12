import sys

cache = {}

def int_overflow(val):
    if not -sys.maxint-1 <= val <= sys.maxint:
        val = (val + (sys.maxint + 1)) % (2 * (sys.maxint + 1)) - sys.maxint - 1
    return val

def calc(x):
    if x in cache:
        return cache[x]

    if x > 4:
        v1 = calc(x - 1)
        v2 = v1 - calc(x - 2)
        v3 = calc(x - 3)
        v4 = v3 - calc(x - 4) + v2
        ret = int_overflow(v4 + 4660 * calc(x - 5))
    else:
        ret = int_overflow(x * x + 9029)

    cache[x] = ret
    return ret

for x in range(0x18e28):
    calc(x)

key = calc(0x18e28)
print(key)

"""
The key generation this time is using a heavily recursive function on a large number.
We can speed this up by generating the keys for all values up to the one that the actual program uses.
This way we can easily find the key in a reasonable amount of time.

gdb-peda$ call (int) decrypt_flag(-2354594148018064674)
$1 = 0x29
gdb-peda$ p (char*) &flag
$2 = 0x601080 <flag> "picoCTF{dynamic_pr0gramming_ftw_d1b4a912}"
"""
