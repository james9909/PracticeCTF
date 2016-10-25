import requests
import time

# Sloppy script to get, sort, and post the data

def decode(string):
    string = string.split(",")
    decoded = []
    for num in string:
        if num != " ":
            decoded += chr(158 - int(num))
        else:
            decoded += " "
    answer = "".join(decoded)
    return answer

url = "https://www.hackthis.co.uk/levels/coding/2"
login = "https://www.hackthis.co.uk/?login"
payload = {"username": "USERNAME", "password": "PASSWORD"}

s = requests.Session() # Start a session
s.post(login, data=payload) # Login
start = time.time()
response = s.get(url).text # Get problem data
problem = response[response.find("<textarea>")+10:response.find("</textarea>")] # Parse for nums
print problem
solution = decode(problem) # Solve problem
print solution
payload = {"answer": solution}
s.post(url, data=payload) # Post data
end = time.time()
response = s.get(url).text
if ("Incomplete" in response):
    print ":("
else:
    print "Sucessfully solved problem"
