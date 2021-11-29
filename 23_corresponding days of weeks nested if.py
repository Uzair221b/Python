# input  a number between 0 to 7 corresponding days of weeks
# @uzair221b
import time
n = int(input('Enter a number between 0 to 7:'))
if n <= 7:
    if n == 1:
        print('Monday')
    if n == 2:
        print('Tuesday')
    if n == 3:
        print('Wednesday')
    if n == 4:
        print('Thursday')
    if n == 5:
        print('Friday')
    if n == 6:
        print('Saturday')
    if n == 7:
        print('Sunday')
else:
    print('Invalid Number')
time.sleep(2)