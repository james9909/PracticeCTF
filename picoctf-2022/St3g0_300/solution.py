from PIL import Image

im = Image.open("pico.flag.png")
width, height = im.size
pixels = im.load()
binary = ""
for x in range(106):
    p = pixels[x, 0]
    binary += str(p[0] & 1)
    binary += str(p[1] & 1)
    binary += str(p[2] & 1)

# picoCTF{7h3r3_15_n0_5p00n_96ae0ac1}
