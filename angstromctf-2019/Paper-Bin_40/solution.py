offsets = [222, 352478, 708830, 1081566, 1446110, 1790174, 2171102, 2531550, 2932958, 3301598, 3629278, 4051166, 4411614, 4739294, 5066974, 5415134, 5751006, 6082782, 6385886, 6770910]

with open("paper_bin.dat", "rb") as f:
    all_bytes = f.read()
    for i in range(len(offsets)):
        if i == len(offsets) - 1:
            extracted = all_bytes[offsets[i]:]
        else:
            extracted = all_bytes[offsets[i]:offsets[i+1]]
        with open("out{}.pdf".format(i), "wb") as pdf:
            pdf.write(extracted)

"""
Looking at the output of `binwalk`, we can find several pdfs embedded within the given file.
We can extract all of those pdfs pretty trivially, since we know all the offsets.
Each pdf is about a different math topic, but if we look through each of them individually, we can
find the flag in out17.pdf.

actf{proof_by_triviality}
"""
