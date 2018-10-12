from PIL import Image

image = Image.open("nowYouDont.png")
width, height = image.size
pixels = image.load()

isolated = Image.new("RGB", (width, height))
isolated_pixels = isolated.load()

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        if pixel != (145, 32, 32, 255):
            isolated_pixels[x, y] = pixel

isolated.save("flag.png")

"""
Looking at the individual pixels of the image, we see that there are actually 2 shades of red.
If we draw a new image with only the pixels that are one of those shades of red, we see the flag.
picoCTF{n0w_y0u_533_m3}
"""
