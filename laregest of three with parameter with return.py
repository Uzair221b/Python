a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = int(input('Enter the value of c'))


def large():
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c


x = large()
print('largest of three number', x)
