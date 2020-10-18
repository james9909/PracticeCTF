enc = "dspttjohuifsvcjdpobqjtwtvk"

for x in range(1, 26):
    candidate = [chr(ord("a") + ((ord(c) - ord("a") + x) % 26)) for c in enc]
    print("".join(candidate))

"""
Since the caesar cipher only has 26 possible shifts, we can brute force each one and
find the one that most resembles a flag.

The flag is picoCTF{crossingtherubiconapisvsuj}
"""
