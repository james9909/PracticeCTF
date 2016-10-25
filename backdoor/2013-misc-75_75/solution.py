import re
import requests
import string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def is_prime(n):
    for x in range(2, n):
        if n%x == 0:
            return False
    return True

def sum_primes(n):
    _sum = 0
    i = 2
    j = 0
    while j < n:
        if is_prime(i):
            _sum += i
            j += 1
        i += 1
    return _sum

url = "http://hack.bckdr.in/2013-MISC-75/misc75.php"
cookies = {"PHPSESSID": "cookie"}

response = requests.get(url, cookies=cookies).text
number = re.search("First (\d+)", response).group(1)
answer = sum_primes(int(number))

data = dict(answer=answer)
response = requests.post(url, cookies=cookies, data=data).text
print response

# 2ac4a6e921c6a5f5f36e8300896b597f9b4f83dc197294ca39fc3a862c734856
