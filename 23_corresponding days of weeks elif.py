# input  a number between 0 to 7 corresponding days of weeks
# @uzair221b
import time
n = int(input('Enter number between 0 to 7:'))
if n >= 7:
    print('Invalid number')
elif n == 5:
    print('Friday')
elif n == 3:
    print('Wednesday')
elif n == 4:
    print('Thursday')
elif n == 6:
    print('Saturday')
elif n == 1:
    print('Monday')
elif n == 7:
    print('Sunday')
elif n == 2:
    print('Tuesday')
time.sleep(2)