f = open("ext-super-magic.img", "rb").read()

bytes = f[:1024 + 56] + "\x53\xEF" + f[1024 + 58:]
open("repaired.img", "wb").write(bytes)

"""
Running e2fsck on the image tells us that there is a bad magic value in the superblock header
which we need to repair. Looking at the file format specification (http://www.nongnu.org/ext2-doc/ext2.html#S-MAGIC),
we see that s_magic needs to have the value 0xEF53. All we need to do is replace whatever
bytes exist at that offset with 0xEF53.

Finally, with debugfs, we can list the contents of the repaired filesystem, with one of the images being
flag.jpg.

picoCTF{a7DB29eCf7dB9960f0A19Fdde9d00Af0}
"""
