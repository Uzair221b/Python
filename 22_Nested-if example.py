# input a number and check if it is between 0 to 25, 25 to 50 or greater than 50
# @uzair221b
import time
n = int(input('Enter a number:'))
if n < 50:
    if n <= 25:
        print('n is less or equals to 25')
    else:
        print('number is between 26 to 50')
else:
    print('number is greater than equals 50')


