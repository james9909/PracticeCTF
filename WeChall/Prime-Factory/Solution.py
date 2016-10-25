# Find the first two primes above 1 million, whose separate digit sums are also prime.
# As example take 23, which is a prime whose digit sum, 5, is also prime.
# The solution is the concatination of the two numbers,
# Example: If the first number is 1,234,567
# and the second is 8,765,432,
# your solution is 12345678765432

def isPrime(num):
    if (num % 2 == 0):
        return False
    i = 3
    while (i * i) < num:
        if num % i == 0:
            return False
        i += 2
    return True

def hasPrimeDigitSum(num):
    num = str(num)
    summ = 0
    for i in num:
        summ += int(i)
    return isPrime(summ)

def firstTwoAbove(number):
    primes = []
    while (len(primes) != 2):
        if(isPrime(number)):
            if(hasPrimeDigitSum(number)):
                primes.append(str(number))
        number += 1
    return primes

def main():
    primes = firstTwoAbove(1000000)
    print primes[0] + primes[1]

if __name__ == '__main__':
    main()
