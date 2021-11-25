import time

let = ['a','b','c','D','e','f','g']
for i in let:
    print(i)
    if i == "e":
        print('found')
        if i == "e":
            print(let)
            break
        
else:
    print('not found')

time.sleep(5)