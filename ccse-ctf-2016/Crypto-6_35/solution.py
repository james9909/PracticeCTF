enc = "123 097 115 099 095 097 110 100 095 105 105 095 115 104 097 108 108 095 114 101 099 101 105 118 101 125".split(" ")

flag = ""
for char in enc:
    flag += chr(int(char))

print flag

# {asc_and_ii_shall_receive}
