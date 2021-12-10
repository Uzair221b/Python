# print number between 1 to 100 that are divisible by 3 and 5 using while loop
# @uzair221b
import time

lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
i = lower
while i <= upper:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i = i + 1

time.sleep(1)
