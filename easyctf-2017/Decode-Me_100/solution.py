f = open("encrypted_flag.txt", "r").readlines()
enc = "".join(f)
while "easyctf" not in enc:
    enc = enc.decode("base64")

print enc

# easyctf{what_1s_l0v3_bby_don7_hurt_m3}
