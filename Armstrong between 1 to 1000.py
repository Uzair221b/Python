t = 0
sum = 0
for i in range(1, 1001):
    if n > 0:
        d = n % 10
        sum = sum + d ** 3
        n = n // 10
if 