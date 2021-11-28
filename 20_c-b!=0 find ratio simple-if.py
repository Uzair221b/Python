# Input the values of a,b,c,d and find the ratio of (a+b) to (c-d) if and only if c-d!=0 with simple-if
# @uzair221b
import time
import math
a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = int(input('Enter the value of c:'))
d = int(input('Enter the value of d:'))
t = c-d
if t != 0:
    r = (a+b) / t
    print('the ration is', r)
if t == 0:
    print('c-d is equals to 0 perhaps ratio could not be find')

time.sleep(1)