# input three numbers and find the largest with nested if
# @uzair221b
import time
a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = int(input('Enter the value of c:'))
if a > b and a > c:
    print(a)
elif b > c and b > a:
    print(b)
else:
    print(c)
