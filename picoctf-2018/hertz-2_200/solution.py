import string

enc = "Usm nxalp ywgeq fgv bxhki gcmw usm tjzd ogr. A ljq'u ymtamcm usai ai ixls jq mjid kwgytmh aq Kalg. Au'i jthgiu ji af A igtcmo j kwgytmh jtwmjod! Gpjd, faqm. Smwm'i usm ftjr: kalgLUF{ixyiuauxuagq_laksmwi_jwm_ugg_mjid_qtwrwehdqq}"
kpt = "The quick brown fox jumps over the lazy dog."

d = {}
for x in range(len(kpt)):
    d[enc[x].upper()] = kpt[x].upper()
    d[enc[x].lower()] = kpt[x]

dec = ""
for char in enc:
    if char in string.punctuation:
        dec += char
    else:
        dec += d[char]

print(dec)

"""
Using quipqiup, we find that the plaintext starts with "The quick brown fox jumps over the lazy dog.", which
contains all the letters we need to solve the rest of the substitution.

The quick brown fox jumps over the lazy dog. I can't believe this is such an easy problem in Pico. It's almost as if I solved a problem already! Okay, fine.
Here's the flag: picoCTF{substitution_ciphers_are_too_easy_nlrgrwmynn}
"""
