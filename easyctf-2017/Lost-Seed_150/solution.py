kpt = "easyctf{"

def pseudorand(x):
    return (x * 19394489 + 132241) & 255

enc = open("flag.out", "r").read().strip()
key = ord(kpt[0]) ^ ord(enc[0])

dec = "e" # Start off with "e"
for x in range(1, len(enc)):
    key = pseudorand(key)
    dec += chr(ord(enc[x]) ^ key)

print dec

# Disassembling the binary, it looks the flag was encrypted using XOR
# First, it generates a random number from /dev/urandom, then uses a function to generate pseudorandom values off of that
# We know that the flag begins with "easyctf{", so we can figure out the first character of the key,
# and then generate the rest of the key if we can reverse the pseudorand() function.

# 0x0000000000400745 <+0>:     push   rbp
# 0x0000000000400746 <+1>:     mov    rbp,rsp
# 0x0000000000400749 <+4>:     mov    eax,DWORD PTR [rip+0x200915]        # 0x601064 <seed>
# 0x000000000040074f <+10>:    imul   eax,eax,0x127efb9
# 0x0000000000400755 <+16>:    add    eax,0x20491
# 0x000000000040075a <+21>:    movzx  eax,al
# 0x000000000040075d <+24>:    mov    DWORD PTR [rip+0x200901],eax        # 0x601064 <seed>
# 0x0000000000400763 <+30>:    mov    eax,DWORD PTR [rip+0x2008fb]        # 0x601064 <seed>
# 0x0000000000400769 <+36>:    pop    rbp
# 0x000000000040076a <+37>:    ret

# From this, we know that the formula looks like (x * 19394489 + 132241), but the numbers
# are too large, so we either need to bitwise and, bitwise or, or use modulo.

# key = [ord(kpt[x]) ^ ord(enc[x]) for x in range(len(kpt))]
# print key

# Looking at the seeds, we can determine that we need to bitwise and by 255.

# Now that we have the pseudorand function, we can decrypt the rest of the flag:

# easyctf{r3ndom_numb3rs_m3an_n0thing_wh3n_y0u_can_brute_force!}
