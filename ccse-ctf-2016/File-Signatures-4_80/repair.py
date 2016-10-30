f = open("filesig_4", "rb").read()[4:]

f = "%PDF" + f

open("repaired.pdf", "wb").write(f)

# The file given to us looks like a pdf, but the first 4 bytes are incorrect, so let's correct them.
# con_eaze
