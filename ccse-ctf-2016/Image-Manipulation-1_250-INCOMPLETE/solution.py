from PIL import Image

image = Image.open("img_man_1.png")
pixels = image.load()
width, height = image.size

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

for img in range(3):
    new = Image.new("RGB", (width, height))
    new_pixels = new.load()
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            p = bin(pixel[img])[-1]
            if p == "1":
                new_pixels[x, y] = WHITE
            else:
                new_pixels[x, y] = BLACK
    new.save("%s.png" % img)
