import itertools

data = "b1d3324cfce6ef5eede466cd57f5e17fcd7f55f6e964e7c97f75e954e64df779fcfc5171f93e18d9".decode("hex")

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def encode(string):
    b = bytearray(string)
    for i in range(0, len(b) - 3):
        block = b[i:i+4]
        print("Block: 0x%s" % str(block).encode("hex"))
        value = (block[0] ^ 0xDE)
        block[0] = value

        print("Before ror: 0x%s" % str(block).encode("hex"))
        value = rol(int(str(block[0:2]).encode("hex"), 16), 16 - 0xD, 16)
        print("After ror: 0x%04x" % value)
        block[0:2] = ("%04x" % value).decode("hex")

        print("Before rol: 0x%s" % str(block).encode("hex"))
        value = rol(int(str(block[::-1]).encode("hex"), 16), 32 - 0xF, 32)
        print("After rol: 0x%08x" % value)
        b[i:i+4] = ("%08x" % value).decode("hex")
        print(str(b[i:i+4]).encode("hex"))
        print("Done encoding block\n")
    return b

print(encode("picoCTF{"))

def to_int(bytes):
    return int(str(bytes).encode("hex"), 16)

def to_str(i):
    return ("%08x" % i).decode("hex")

data = bytearray(data)
for x in reversed(range(0, len(data) - 3)):
    block = str(data[x:x+4])
    value = to_int(block)
    value = ror(value, 0xF, 32)

    value_str = to_str(value)
    lower_bytes = rol(to_int(value_str), 0xD, 16)
    value_str = to_str(lower_bytes) + value_str[2:]

    value = to_int(value_str) ^ 0xDE
    data[x:x+4] = ("%08x" % value).decode("hex")

print(data)
