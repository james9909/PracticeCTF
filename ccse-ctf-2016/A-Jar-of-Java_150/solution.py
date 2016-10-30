enc = [81, 89, 95, 73, 66, 117, 66, 75, 88, 78, 117, 64, 75, 92, 75, 87]

flag = ""

for char in enc:
    flag += chr(char ^ 0x2a)

print flag

# We can decompile the class file within the jar to see the source.
# Inside, we see an array of integers that is xor'd by 0x2a then compared against the user's input.
# This script decrypts xor the flag:

# {such_hard_java}
