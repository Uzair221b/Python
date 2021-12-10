a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))


def large():
    if a > b:
        return a
    else:
        return b


x = large()
print(x)

