enc = "10010111 10001011 10001011 10001111 11000101 11010000 11010000 10001100 10010110 10011000 10010001 10010110 10010001 11010001 10011100 10011110 10010010 10001100 10011100 10001100 10011100 11010001 10010000 10001101 10011000".replace(" ", "")

enc = enc.replace("1", "a").replace("0", "1").replace("a", "0")

hex_string = hex(int(enc, 2))[2:-1]
print hex_string.decode("hex")

# http://signin.camscsc.org
# Server was taken down, so challenge is no longer solvable :(
