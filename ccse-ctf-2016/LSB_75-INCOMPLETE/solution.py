from PIL import Image

image = Image.open("galaxy.png")
width, height = image.size
pixels = image.load()

new = Image.new("RGB", (width, height))
new_pixels = new.load()

lsb = ""

for x in range(width):
    for y in range(height):
        r = int(bin(pixels[x, y][0])[-1])
        g = int(bin(pixels[x, y][1])[-1])
        b = int(bin(pixels[x, y][2])[-1])

        new_pixels[x, y] = (r, g, b)
        print new_pixels[x, y]

new.save("out.png")
# print ''.join(chr(int(lsb[i:i+8], 2)) for i in xrange(0, len(lsb), 8))
