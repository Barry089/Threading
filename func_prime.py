
from math import sqrt

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0: return False

    return True

m = int(input("Please input a number: "))
if is_prime(m):
    print("%d 是素数。" % m)
else:
    print("%d 不是素数。" % m)
