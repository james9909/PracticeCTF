import string

msg = map(int, "268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186".split(" "))
flag = ""
for char in msg:
    char = pow(char, -1, 41)
    if char <= 26:
        flag += string.ascii_letters[char-1]
    elif char <= 36:
        flag += string.digits[char - 27]
    else:
        flag += "_"

print(f"picoCTF{{{flag}}}")

# picoCTF{1nv3r53ly_h4rd_c680bdc1}
