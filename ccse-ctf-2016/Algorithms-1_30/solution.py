from PIL import Image

image = Image.open("algo_1.png")
width, height = image.size
pixels = image.load()

flag = ""

BLACK = (0, 0, 0)

for y in range(height):
    for x in range(width):
        if pixels[x, y] == BLACK:
            flag += chr(x + ord("a") - 1)

print flag

# thisisthesuperlongflagthatihopeyouhopefullydidnotpulloutmanually
