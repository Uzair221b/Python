# Input three numbers and perform addition of last digit of each number
# "BY @uzair221b"
import time
import math
a = int(input('Enter the first number'))
b = int(input('Enter the second number'))
c = int(input('Enter the third number'))
p = a % 10
q = a % 10
r = a % 10
add = p+q+r
print('Addition of last digits of your three inputs', add)
time.sleep(1)