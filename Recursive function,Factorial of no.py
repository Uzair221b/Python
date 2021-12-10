# recursive function,factorial of a number
# uzair221b
import time


def rec(n):
    if n == 1:
        return 1
    else:
        return n * rec(n - 1)


n = int(input('Enter a number:'))
f = rec(n)
print('Factorial of a number is:', f)
time.sleep(1)
