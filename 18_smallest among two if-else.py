# Input two numbers and find the smallest with if-else
# @uzair221b
import time
a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
if a < b:
    print(a, 'is smaller than', b)
else:
    print(b, 'is smaller than', a)
    print('End of program')
time.sleep(5)