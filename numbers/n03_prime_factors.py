from sys import argv

script, num = argv
num = int(num)

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            if d not in factors:
                factors.append(d)
            n /= d
        d += + 1

    for item in factors:
    	print item,

prime_factors(num)