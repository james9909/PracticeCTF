enc = '\x15\x02\x07\x12\x1e\x100\x01\t\n\x01"'

first = "actf{coffee_"

second = ""
for x in range(len(first)):
    second += chr(ord(first[x]) ^ ord(enc[x]))
print(first + second)

"""
The encryption scheme used is a simple xor between the two halves of the plaintext.
Xor is reversible, so if we can guess one half of the plaintext, we can decode the other half.
Knowing the flag format, we can guess the first 5 characters: actf{, as well as the last one: }

This decodes to a plaintext that looks something like
actf{xxxxxxxtastexxxxxx}

We can do some manual decoding and guesswork to determine that "taste" is a part of "tastes",
which reveals another character:
actf{cxxxxxxtastesxxxxx}

Some more guesswork reveals that there is an underscore after "tastes":
actf{coxxxxxtastes_xxxx}

With this, we can guess the entire flag:

actf{coffee_tastes_good}
"""
