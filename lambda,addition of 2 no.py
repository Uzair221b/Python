# perform addition of two numbers using lambda function
# uzair221b
import time
add = lambda a, b: a + b

a = int(input('Enter a value of a:'))
b = int(input('Enter a value of b:'))

add = add(a, b)

print('Addition', add)

time.sleep(1)
