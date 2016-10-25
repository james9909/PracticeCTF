def generateKey():
    i = 1
    x = 196
    n = 5493
    while (i <= 25):
        x = (x * i) % n
        i += 1
    key = "flag_" + str(abs(x))
    print key

generateKey()
