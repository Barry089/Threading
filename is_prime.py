
# 判断用户输入的某个数是否是素数

from math import sqrt

n = int(input("Please input a number: "))

flag = 1

if n == 1:
    flag = 0
else:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            flag = 0
            break

if flag == 0:
    print("The Number %d is not a prime." % n)
else:
    print("The Number %d is a prime. " % n)
