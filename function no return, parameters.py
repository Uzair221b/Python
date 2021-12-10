import time


def sub (a, b):
    c = a - b
    print('Subtraction', c)


a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
sub(a, b)
time.sleep(2)
