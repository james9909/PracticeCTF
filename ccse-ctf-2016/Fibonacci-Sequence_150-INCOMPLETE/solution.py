cache = {}

def memoize(f):
    def wrapper(*args, **kwargs):
        key = ",".join(map(str, sorted(args)))
        cached_result = cache.get(key)
        if cached_result:
            return cached_result
        result = f(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def is_palindrome(n):
    return str(n) == str(n)[::-1]

_sum = 0

for x in range(100000):
    n = fibonacci(x)
    if is_palindrome(n):
        print n
        _sum += n

print _sum
# print sum([fibonacci(n) for n in range(9001) if is_palindrome(fibonacci(n))])
