from PIL import Image

image = Image.open("algo_2.png")
pixels = image.load()
width, height = image.size

distance = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

flag = ""

for x in range(width):
    pixel = pixels[x, 0]
    if pixel == WHITE:
        distance += 1
    else:
        flag += chr(distance)
        distance = 1

print flag

# anotheroneofthemsuperlongonesexceptthisoneiswayhardertopullout
