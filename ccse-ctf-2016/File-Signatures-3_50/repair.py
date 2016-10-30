f = open("filesig_3.jpg", "rb").read()[1:-1]

f = "\x89" + f + "\x82"

open("repaired.png", "wb").write(f)

# Looking at the data, it appears that we are given a png, but the header and footer are broken.

# A png is supposed to begin with "89 50 4e 47 0d 0a 1a 0a" and end with "44 ae 42 60 82".
# The first and last byte of the given file are "88" and "81". Change them back to their proper values to repair the png.

# {fil3_r3c0v3ry}
