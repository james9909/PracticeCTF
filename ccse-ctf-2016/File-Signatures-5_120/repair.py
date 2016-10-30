f = open("filesig_5", "rb").read()

f = "\xff\xd8" + f

open("repaired.jpg", "wb").write(f)

# The last couple of bytes are "ff d9", so we know we're probably dealing with a jpg.
# The first 2 header bytes are missing, so just prepend them to the given file to make a valid jpg.

# such_difficulty_123
