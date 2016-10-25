import requests

url = "http://www.wechall.net/challenge/training/programming1/index.php?action=request"
dest = "http://www.wechall.net/challenge/training/programming1/index.php?answer="
headers = {"Cookie": "WC=8630435-16468-hnTDIslza1hhRV7e"}

string = requests.get(url, headers=headers).text
print string

response = requests.get(dest + string, headers=headers).text
print response
