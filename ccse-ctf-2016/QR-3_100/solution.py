from PIL import Image

image = Image.open("qrchal3.png")
width, height = image.size

new = Image.new("RGB", (width, height), "white")

pixels = image.load()
new_pixels = new.load()

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        if pixel == BLACK or pixel == WHITE:
            pass
        else:
            new_pixels[x, y] = BLACK

new.save("qrchal3-extracted.png")

# tiny qr code
# u_mad_bro?
