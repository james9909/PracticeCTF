from PIL import Image

image = Image.open("qr1.bmp")
width, height = image.size
pixels = image.load()

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        if pixel == (254, 254, 254):
            pixels[x, y] = (0, 0, 0)
        elif pixel == (1, 1, 1) and (x <= 120 or x >= 250):
            # Only change the "black" pixel values for the alignment squares
            pixels[x, y] = (255, 255, 255)

image.save("repaired.png")

# easyctf{n0w_who-w0u1d_do_thAT_to_Th3ir_QR?}
