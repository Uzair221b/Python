import time


def sphere(r):
    a = 4 * 3.14 * r * r
    v = 4 // 3 * 3.14 * r * r * r
    print('Area of volume of sphere', a, v)
    r = float(input('Enter the value of area and volume of sphere'))

    sphere(r)


time.sleep(1)
