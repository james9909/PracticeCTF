f = open("flag", "rb").read()[1:]

f = "\x89" + f

open("flag.png", "wb").write(f)

# We can extract the "flag" file by either mounting the image.
# $ mkdir /tmp/mount-it && sudo mount mount_it.dd /tmp/mount-it

# Looking at the bytes, it appears that it's a png. However, the first byte is incorrect.
# We can correct the first byte and view the repaired image to get the flag.

# {MoUnT_i_CaN}
