# Calculate volume of rectangle room using lambda function
# uzair221b
import time

volume = lambda l, b, h : l * b * h

l = int(input("Enter the value of length"))
b = int(input("Enter the value of breath"))
h = int(input("Enter the value of height"))

result = volume(l, b, h)
print('volume of rectangle room is:', result)

time.sleep(1)