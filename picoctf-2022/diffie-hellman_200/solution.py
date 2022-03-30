p = 13
g = 5

a = 7
b = 3

A = pow(g, a, p)
B = pow(g, b, p)

key = pow(B, a, p)
print(key)

# The key is 5, so we can just input this into a caesar cipher decoder online.
# picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_84AA1DA8}
