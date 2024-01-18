import RSAEncoding as rsa
import math
import random

COMPOSITE = 0
PRIME = 1

def pseudoprime(x):
    if rsa.MODPOWER(2, x-1, x) != 1:
        return COMPOSITE
    else:
        return PRIME

def randomprime(n, s):
    for _ in range(s * math.ceil(math.log(n))):
        x = random.randrange(1, n+1)
        if pseudoprime(x) == PRIME:
            return x
    return -1

if __name__ == "__main__":
    print(randomprime(17, 21))