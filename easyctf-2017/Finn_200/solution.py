import operator

from itertools import cycle, izip
from PIL import Image

kylo1 = Image.open("kylo1.png")
kylo2 = Image.open("kylo2.png")

width, height = kylo1.size

diff = Image.new("RGB", (width, height))
diff_pixels = diff.load()

kylo1_pixels = kylo1.load()
kylo2_pixels = kylo2.load()

for y in range(height):
    for x in range(width):
        p1 = kylo1_pixels[x, y]
        p2 = kylo2_pixels[x, y]
        if p1 != p2:
            sub = map(operator.sub, p2, p1)
            if sub != [1, 1, 1]:
                print sub, x, y
            #diff_pixels[x, y] = (255, 255, 255)

diff.save("diff.png")

# Scanning the qr code: \x63\x68\x66\x63\x7e\x71\x73\x34\x76\x57\x72\x3c\x74\x73\x5c\x31\x75\x5d\x6b\x32\x34\x77\x59\x38\x4c\x7f

key = []
for x in range(144, 170):
    p1 = kylo1_pixels[x, 533]
    p2 = kylo2_pixels[x, 533]
    key.append(map(operator.sub, p2, p1)[0])

enc = "\x63\x68\x66\x63\x7e\x71\x73\x34\x76\x57\x72\x3c\x74\x73\x5c\x31\x75\x5d\x6b\x32\x34\x77\x59\x38\x4c\x7f"

def xor(message, key):
    return "".join(chr(ord(c)^k) for c,k in izip(message, cycle(key)))

print xor(enc, key)

# Inside the given image, we find a zip file. We can extract it like any other, but it requires a password.
# Looking at help.txt, we are told to look at the title, which is "Finn". Combined with the hint, we can guess
# that the password is 2187, after FN-2187, which is Finn's stormtrooper code name.
# After that, we are told to view the difference between the extracted files pictorially, which gives us a QR code.

# Reading more from help.txt, we know that flag has been xor'd, and that we need to find the key within the pixel differences.
# Refer to this script for the steps

# flag{st4r_w4rs_1s_b35t_:D}
