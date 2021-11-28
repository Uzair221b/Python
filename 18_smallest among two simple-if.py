# Input two numbers and find the smallest with simple- if
# @uzair221b
import time
a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
if a < b:
    print(a, 'is smaller than', b)
if b < a:
    print(b, 'is smaller than', a)
    print('End of program')
time.sleep(5)