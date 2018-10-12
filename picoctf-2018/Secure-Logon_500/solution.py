import base64
import requests

cookie = "KDOrZiU7t9DSJONkagVvkuMK5LKAeU+xMhQ2VjLWkl72DI/9+xBOullX/HMUZlkqAAeMupgjlkyb+mexmLT53aSpvsvxjJ/fIGd6W9C0xPU=".decode("base64")
for x in range(16):
    print(x)
    candidate = cookie[:x] + chr(ord(cookie[x]) ^ 1) + cookie[x+1:]
    cookies = {
        "cookie": base64.b64encode(candidate)
    }
    r = requests.get("http://2018shell3.picoctf.com:13747/flag", cookies=cookies)
    if "picoCTF" in r.text:
        print(r.text)

"""
The vulnerability here lies in the PyCrypto version, which is 2.6.1.
It turns out that if the IV is not authenticated, an attacker can modify it to flip arbitrary bits
in the plaintext. This attack also seems more relevant when we see that the method
of determining whether or not a user is an admin is through an integer field in the cookie json.
All we need to do is brute force all the possible single bit flips in the IV and check if
we're authenticated.

picoCTF{fl1p_4ll_th3_bit3_7d7c2296}
"""
