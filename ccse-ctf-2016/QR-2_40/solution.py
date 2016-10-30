from PIL import Image

broken = Image.open("qrchal2.png")
width, height = broken.size
fixed = Image.new("RGB", (width, height))

broken_pixels = broken.load()
new = fixed.load()

WHITE = (0, 0, 0, 255)
BLACK = (255, 255, 255, 255)

for x in range(width):
    for y in range(height):
        if broken_pixels[x, y] == BLACK:
            new[x, y] = WHITE
        else:
            new[x, y] = BLACK

fixed.save("qrchal2-fixed.png")


# $ zbarimg qrchal1-fixed.png
# QR-Code:9x18n37198471x
# scanned 1 barcode symbols from 1 images in 0.01 seconds
