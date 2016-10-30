import hashlib
import string

hashes = open("irreversible.txt", "r").read().split()

rainbow = {}
for char in string.printable:
    hashed = hashlib.md5(char).hexdigest()
    rainbow[hashed] = char

flag = ""

for _hash in hashes:
    if _hash in rainbow:
        flag += rainbow[_hash]
    else:
        print "failed"
        break

print flag

# Each hash represents one character of the flag, something we can easily look up
# {much_reversible}
