f = open("message.txt").read().strip()

def chunks(m, n):
    for i in range(0, len(m), n):
        yield m[i:i+n]

decoded = ""
for chunk in chunks(f, 3):
    decoded += chunk[2] + chunk[:2]

print(decoded)

# The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
