enc = open("elif", "r").read()
open("flag.png", "w").write(enc[::-1])

# Looking at the bytes, we see some header bytes resembling a PNG at the bottom, but in reverse
# If we reverse all the bytes, we can restore the elif to its original state and view the flag (which is also in reverse)

# easyctf{r3v3r5ed_4ensics}
