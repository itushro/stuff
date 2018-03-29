import math

def sieve(x):
    x = math.ceil(x)
    p = [i for i in range(x)]
    p[0] = None
    p[1] = None
    for i in p:
        if i:
            m = 2
            while m*i < x:
                p[m*i] = None
                m += 1
    p = [i for i in p if i]
    return p

def check_prime(x):
    y = math.sqrt(x)
    if all(x % i != 0 for i in sieve(y)):
        return True
    else:
        return False

