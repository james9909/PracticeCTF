import string

msg = map(int, "54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288".split(" "))
flag = ""
for char in msg:
    char = char % 37
    if char <= 25:
        flag += string.ascii_uppercase[char]
    elif char <= 35:
        flag += string.digits[char - 26]
    else:
        flag += "_"

print(f"picoCTF{{{flag}}}")

# picoCTF{R0UND_N_R0UND_79C18FB3}
