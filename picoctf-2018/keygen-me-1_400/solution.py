import subprocess
import itertools

def run(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = process.communicate()
    return output[0]

charset = "0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ"
for key in itertools.product(charset, repeat=16):
    key = "".join(key)
    output = run("./activate " + key)
    if "Successfully" in output:
        print(key)
        break

"""
There are many possible keys, so it's pretty easy to just brute force the possibilities for a valid
product key.

The first one I generated is 000000000000000C

Product Activated Successfully: picoCTF{k3yg3n5_4r3_s0_s1mp13_3718231394
"""
