import re

from pwn import *

HOST = "wayward.tcp.easyctf.com"
PORT = 8580
KEY = "6df9796673b7f7540d02387c5dd8fe35"

def shoot(x, y):
    r = remote(HOST, PORT)
    r.recv(1024)
    r.sendline(KEY)
    r.recv(1024)
    r.recv(1024)
    r.sendline("(%s, %s)" % (x, y))
    response = r.recv(1024)
    r.close()
    offset = re.search("You missed. You were \((.*), (.*)\)", response)
    if offset:
        return False, (float(offset.group(1)), float(offset.group(2)))
    else:
        try:
            # recv is janky sometimes
            response = r.recv(1024)
        except:
            pass
        return True, response

while True:
    _, (x0, y0) = shoot(0, 0)
    print "Original position: (%s, %s)" % (x0, y0)
    _, (x1, y1) = shoot(x0, y0)
    print "Offset: (%s, %s)" % (x1, y1)
    x2, y2 = x0 + x1*2, y0 + y1*2
    print "Shooting to: (%s, %s)" % (x2, y2)
    success, response = shoot(x2, y2)
    if success:
        print response
        break
    else:
        # May fail because of the time it takes to connect to the server
        print "[*] Prediction failed."

"""
The space junk seems to travel in a predictable orbit, so as long as we can find its original location
at any given time, we can add some sort of offset and predict its next location.

Our first shot tells us the location of the space junk, and our second shot tells us how far it traveled after the
first shot. For our third shot we can try shooting to the original location with two offsets added (to account for the distance
traveled after the second shot)

$ python solution.py
[+] Opening connection to wayward.tcp.easyctf.com on port 8580: Done
[*] Closed connection to wayward.tcp.easyctf.com port 8580
Original position: (9616.129, -5534.988)
[+] Opening connection to wayward.tcp.easyctf.com on port 8580: Done
[*] Closed connection to wayward.tcp.easyctf.com port 8580
Offset: (21.589, 45.246)
Shooting to: (9659.307, -5444.496)
[+] Opening connection to wayward.tcp.easyctf.com on port 8580: Done
[*] Closed connection to wayward.tcp.easyctf.com port 8580
Perfect!
Your flag is: easyctf{8e74ff6519c207bf556d8cce03a220ad}
"""
