n = float(open("/dev/std%sn" % chr(105), "r").read())

a = ["", "F%szz" % chr(105)]
b = ["", "Buzz"]

stdout = open("/dev/stdout", "w")
wrte = getattr(stdout, "wr%ste" % chr(105))

def fzz(x):
    s = ""
    s += a[x%3 == 0]
    s += b[x%5 == 0]
    s = s or str(x)
    wrte(s + "\n")
    x < n and fzz(x+1)

fzz(1)
