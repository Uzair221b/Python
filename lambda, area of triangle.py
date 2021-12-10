# Calculate area of triangle using lambda function
# uzair221b

import time

area = lambda b, h : 1.5 * b * h

b = int(input("Enter the value of breath"))
h = int(input("Enter the value of height"))

result = area (b,h)
print('Area of triangle is:', result)

time.sleep(1)