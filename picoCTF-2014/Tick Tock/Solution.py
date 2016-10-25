import fractions

secretz = [(1, 2), (2, 3), (8, 13), (4, 29), (130, 191), (343, 397), (652, 691), (858, 1009),(689, 2039), (1184, 4099), (2027, 7001), (5119, 10009), (15165, 19997), (15340, 30013),(29303, 70009), (42873, 160009), (158045, 200009)]

# Crack the password
def pass_crack():
    result = 1
    const = 1

    for (r,m) in secretz:
        while result % m != r:
            result += const
        const *= m

    print "Password is %d" % result

pass_crack()
print "Signature is %d" % 32002880064
# The second part is Euler's totient, so if we use a totient calculator on
# 2000009*160009(32003240081), we get the answer to the second part, which is 32002880064
