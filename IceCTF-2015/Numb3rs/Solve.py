def toASCII(number):
    newString = ""
    if len(number) % 2 != 0:
        print "Not in pairs!"
        return
    while len(number) != 0:
        temp = int(number[:2])
        temp += 97 # Account for shift, resulting in a = 0, b = 1, c = 2, etc.
        newString += chr(temp)
        number = number[2:]
    return newString

def main():
    cipher = "05110006_00111507000104190802_08130308020418".split("_")
    print "_".join([toASCII(word) for word in cipher])

main()
