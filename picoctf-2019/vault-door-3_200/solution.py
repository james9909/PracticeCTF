enc = "jU5t_a_sna_3lpm17ga45_u_4_mbrf4c"
dec = [ord(c) for c in enc]

for i in range(8):
    dec[i] = enc[i]

for i in range(8, 16):
    dec[23 - i] = enc[i]

for i in range(16, 32, 2):
    dec[46 - i] = enc[i]

i = 31
while i >= 17:
    dec[i] = enc[i]
    i -= 2

password = "".join(dec)
print("picoCTF{{{}}}".format(password))

"""
Looking at the checkPassword function, we see that it just shuffles characters around.
We can easily un-shuffle these characters to get the original flag back:

picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_5baf7c}
"""
