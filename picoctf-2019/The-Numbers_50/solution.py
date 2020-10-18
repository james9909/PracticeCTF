numbers = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }".split(" ")

dec = ""
for char in numbers:
    if char == "{" or char == "}":
        dec += char
    else:
        dec += chr(int(char) - 1 + ord("A"))
print(dec)

"""
Each number in the image represents an uppercase ASCII letter, as mentioned in the hint.
Converting all of the numbers to letters, we get the flag:
PICOCTF{THENUMBERSMASON}
"""
