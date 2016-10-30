from PIL import Image

def decode(binary_string):
    return hex(int(binary_string, 2))[2:-1].decode("hex")

image = Image.open("image-ception.png")
width, height = image.size

pixels = image.load()

r = ""
g = ""
b = ""

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        print bin(pixel[2])
        # r += bin(pixel[0])[-2]
        # g += bin(pixel[1])[-2]
        # b += bin(pixel[2])[-2]

# print decode(r)
# print decode(g)
# print decode(b)
