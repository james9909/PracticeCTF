from PIL import Image

image = Image.open("qrchal5.png")
width, height = image.size
pixels = image.load()

new = Image.new("RGB", (width, height))
new_pixels = new.load()

WHITE = (255, 255, 255)
BLACK = (40, 40, 40)

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        if pixel != WHITE and pixel != BLACK:
            print pixel
            # new_pixels[x, y] = BLACK
            # print pixel
        else:
            pass
            # new_pixels[x, y] = pixel

# new.save("fixed.png")
