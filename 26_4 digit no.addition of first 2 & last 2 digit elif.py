# input  a number between 0 to 7 corresponding days of weeks
# @uzair221b
import time
n = int(input('Enter a number:'))
if (n >= 999) and (n <= 9999):
    a = n // 100
    b = n % 100
    c = a + b
    print(c)
else:
    print('Enter a 4 digit number')
time.sleep(1)
