from z3 import Solver, BitVec, sat

s = Solver()
q = [BitVec("q_%s" % (i),16) for i in range(17)]

s.add([q[x] >= 33 for x in range(17)])
s.add([q[x] <= 125 for x in range(17)])

s.add(q[16] ^ 128 == 253)
s.add(q[0] & q[16] == 121)
s.add((q[0] + 2) % 5 == 0)
s.add(q[11] == 95)
s.add((q[5] >> (q[16] - q[0])) == 16)
s.add((q[5] << (q[16] - q[0])) == 260)
s.add(q[13] ^ q[11] == 110)
s.add((q[13] * 1.0 / q[10]) == 7/11.0) # Floating points :(
s.add(((q[13] & q[11]) * 4) + 1 == q[6])
s.add(q[5] & q[13] <= 17)
s.add(q[1] - 9 == q[9])
s.add((q[7] & q[9]) == q[11] + (q[5] & q[13]))
s.add(q[7] % 57 == 0)
s.add((q[9] + q[11]) / 2 == q[12])
s.add(q[7] ^ q[3] == q[11])
s.add(q[3] ^ q[8] == 0)
s.add(q[15] & q[3] == q[9] & q[8])
s.add(q[15] >> 3 == 6)
s.add(q[15] % 5 == 3)
s.add(q[4] ^ q[7] == q[5] - q[8])
s.add(q[2] & q[8] == 32)
s.add(q[2] << 2 == q[0] + q[6])
s.add(q[14] % 29 == 0)
s.add(q[14] % 9 == 8)

s.add(q[10] == 77) # We know the ratio between q[13] and q[10] is 7/11, and that q[13] is likely 49. Thus, q[10] has to be 77.

flag = ""

if s.check() == sat:
    m = s.model()
    print m
    chars = [m.evaluate(q[i]) for i in range(len(q))]
    for char in chars:
        try:
            flag += chr(int(str(char)))
        except:
            flag += "."

    print flag
else:
	print "failed"

# {n0-fAEr-eM_b1t5}
