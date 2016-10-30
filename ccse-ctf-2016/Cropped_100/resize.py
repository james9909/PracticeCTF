def encode(n):
    first = hex(n / 256)[2:]
    second = hex(n % 256)[2:]
    if len(first) == 1:
        first = "0" + first
    if len(second) == 1:
        second = "0" + second

    return [first.decode("hex"), second.decode("hex")]

f = open("cropped.png", "rb").read()

new_width = 675
new_height = 800

f = list(f)
f[18:20] = encode(new_width)
f[22:24] = encode(new_height)

f = "".join(f)

expected_checksum = "ecc14614".decode("hex")
# Acquired after running 'pngcheck' on the modified image
new_checksum = "20129b98".decode("hex")
f = f.replace(expected_checksum, new_checksum)

open("resized.png", "wb").write(f)

# Modify the bytes that represent the height of the image and recompute the CRC checksum to successfully resize the image.
# Flag: 1fvLf$&#VXa
