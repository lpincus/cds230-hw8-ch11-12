#
# 7. Using the random dart method 
#   show that the area of a right triangle 
#   is half of the area of the bounding box. 

import random
side = 1
total = 0
intri = 0
for i in range(1000000):
    total = total + 1
    x = random.random()
    y = random.random()
    if x + y < side:
        intri = intri + 1

print(intri / float(total))
