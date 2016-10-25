import requests

# Sloppy script to get, sort, and post the data

def sort(string):
    string = string.split(", ")
    return ", ".join(sorted(string))

url = "https://www.hackthis.co.uk/levels/coding/1"
login = "https://www.hackthis.co.uk/?login"
payload = {"username": "USERNAME", "password": "PASSWORD"}

s = requests.Session() # Start a session
s.post(login, data=payload) # Login
response = s.get(url).text # Get problem data
problem = response[response.find("<textarea>")+10:response.find("</textarea")] # Parse for words
solution = sort(problem) # Solve problem
payload = {"answer": solution}
s.post(url, data=payload) # Post data
response = s.get(url).text
if ("Incomplete" in response):
    print ":("
else:
    print "Sucessfully solved problem"
