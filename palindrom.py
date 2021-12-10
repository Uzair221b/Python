n = int(input('Enter a number'))
t = n
r = 0
while n > 0:
    d = n % 10
    r = r * 10 + d
    n = n // 10
if r == t:
    print('number is palindrome', r)
else:
    print('number is not palindrome', r)
