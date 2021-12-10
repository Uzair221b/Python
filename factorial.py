# input a number and find its factorial
# @uzair221b
n = int(input('Enter a number'))
f = 1
for i in range(1, n+1):
    f = f * i
print(f)