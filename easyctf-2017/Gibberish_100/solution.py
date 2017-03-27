import itertools

from PIL import Image

image = Image.open("gibberish.png")
width, height = image.size
pixels = image.load()

def part_1():
    binary = ""
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if pixel[0] != 0:
                binary += "1"
            else:
                binary += "0"
    binary = int(binary[:64], 2) # Repeats every 64 characters
    print ("%x" % binary).decode("hex")

def part_2():
    part2 = Image.new("RGB", (width, height))
    p2_pixels = part2.load()
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if pixel[1] != 0:
                p2_pixels[x, y] = (0, 0, 0)
            else:
                p2_pixels[x, y] = (255, 255, 255)

    part2.save("part2.png")

def part_3():
    binary = ""
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if pixel[2] != 0:
                binary += "1"
            else:
                binary += "0"
    binary = int(binary[:64], 2) # Repeats every 64 characters
    print ("%x" % binary).decode("hex")

part_1() # aPgMasSt
part_2() # LH5i6uQz (Scan with a barcode scanner)
part_3() # 5U5EYz2b

"""
The problem description tells us that there are 3 parts to the flag, so that means that the
flag is probably hidden in each of the R, G, and B values
The hint tells us that we should only care about the presence of the RGB values, not their actual value.

The check the presence of the red and blue to form two binary strings, and we
check the presence of green to create a barcode image.

Each of the parts decodes to an 8 character string for a pastebin paste.
http://pastebin.com/raw/aPgMasST:  easyctf{col0rs_
http://pastebin.com/raw/LH5i6uQz:  b4rcod3s_
http://pastebin.com/raw/5U5EYz2b:  and_b1nary_f?n}

easyctf{col0rs_b4rcod3s_and_b1nary_f?n}
"""
