# Calculate perimeter of triangle using lambda function
# uzair221b

import time

perimeter = lambda l, b : 2 * l * b

l = int(input("Enter the value of length"))
b = int(input("Enter the value of breath"))

result = perimeter (l, b)
print('perimeter of rectangle is:', result)

time.sleep(1)