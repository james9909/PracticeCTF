count = 0

for x in range(1, 1000000):
    if "11" not in bin(x):
        count += 1

print count

# 17710
