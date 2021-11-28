# Input two numbers and perform addition if first no is greater than second number otherwise perform subtraction with
# if-else
# @uzair221b
import time
import math
a = int(input('Enter the first number'))
b = int(input('Enter the second number'))
if a > b:
    c = a+b
    print('First number is greater perhaps addition has been performed', c)
else:
    c = a-b
    print('First number is smaller perhaps subtraction has been performed', c)
time.sleep(1)