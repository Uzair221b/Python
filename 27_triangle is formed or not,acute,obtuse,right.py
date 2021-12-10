# input 3 angles of a triangle and check if it formed or not , if yes check it is acute,obtuse or right angle triangle
# @uzair221b
import time
a = int(input('Enter the value a:'))
b = int(input('Enter the value b:'))
c = int(input('Enter the value c:'))
sum = a+b+c
if sum == 180:
    print('Triangle has formed')
    if a > 90 and b > 90 and c > 90:
        print('It is acute triangle')
    elif a > 90 or b > 90 or c > 90:
        print('It is obtuse triangle')
    else:
        print('It is right angle triangle')
else:
    print('Triangle has not formed ')
time.sleep(1)