# input  a number between check if it is 3 digit number if yes, perform addition of first and last digit
# @uzair221b
import time
n = int(input('Enter a number:'))
if (n >= 99) and (n <= 999):
    first = n % 10
    second = n // 100
    add = first + second
    print('Addition of first and last digit is:', add)
else:
    print('Please enter a three digit number')
time.sleep(1)