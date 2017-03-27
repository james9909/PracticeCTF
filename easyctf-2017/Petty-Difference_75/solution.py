f1 = open("file1.txt", "r").read()
f2 = open("file2.txt", "r").read()

flag = ""

for x in range(len(f1)):
    if f1[x] != f2[x]:
        flag += f1[x]

print flag[::-1]

# The flag is hidden in the difference between the two files. Just take the characters
# that are present in file1.txt but not in file2.txt and reverse the string
# easyctf{th1s_m4y_b3_th3_d1ff3r3nc3_y0u_w3r3_l00k1ng_4}
