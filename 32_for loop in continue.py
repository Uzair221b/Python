# for loop in continue
# @uzair221b
import time
l = ["Divergent", "Insurgent", "Elegant"]
for i in l:
    if i == "Insurgent":
        continue
    print(i)
time.sleep(1)