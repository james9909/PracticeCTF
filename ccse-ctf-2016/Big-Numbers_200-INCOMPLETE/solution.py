def is_palindrome(n):
    return str(n) == str(n)[::-1]

s = 0
count = 0

start = 100000000
while count <= 9001:
    print start
    if is_palindrome(start):
        count += 1
        s += start
    start += 1

print s
