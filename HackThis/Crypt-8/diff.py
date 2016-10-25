from PIL import Image

logo = Image.open("c8.png")
logo_pixels = logo.load()
keith = Image.open("extracted.png")
keith_pixels = keith.load()
difference = Image.new('RGB', logo.size, (255, 255, 255))
difference_pixels = difference.load()

height, width = logo.size
for r in range(height):
    for c in range(width):
        p = logo_pixels[r,c]
        k = keith_pixels[r,c]
        new = []
        for num in range(3):
            temp = p[num] + k[num]
            new += temp

        difference_pixels[r,c] = new
        '''
        difference_pixels[r,c] = (0 if abs(p[0]-k[0]) > 2 else 255,
                                  0 if abs(p[1]-k[1]) > 2 else 255,
                                  0 if abs(p[2]-k[2]) > 2 else 255)
        '''

difference.save("difference.png")
