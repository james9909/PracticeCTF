n = input()

for x in range(1, n+1):
    s = ""
    if x % 3 == 0:
        s += "Fizz"
    if x % 5 == 0:
        s += "Buzz"
    print s or x
