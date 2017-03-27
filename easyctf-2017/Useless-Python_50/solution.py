enc = open("useless.py", "r").read().strip()
enc = enc.decode("hex")
while "easyctf" not in enc:
    enc = eval(enc[5:-1])
print enc

# Decoding the initial contents of the file gives us more python code.
# We can't just eval the python code, because it is wrapped in an exec() call.
# However, we CAN remove the exec call and eval its contents.
# Eventually, it decodes into:

# flag = 'easyctf{python_3x3c_exec_3xec_ex3c}'
# priint flag

# easyctf{python_3x3c_exec_3xec_ex3c}
