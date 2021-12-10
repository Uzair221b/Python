import time


def div(a, b):
    c = a - b
    print('Subtraction', c)


a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
div(a, b)
time.sleep(2)
