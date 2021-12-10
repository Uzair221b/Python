n = int(input('Enter a number'))
t = n
sum = 0
while n > 0:
    d = n % 10
    sum = sum + d ** 3
    n = n // 10
if sum == t:
    print('number is armstrong', t)
else:
    print("number is not armstrong number", t)