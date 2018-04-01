# 8. Using the random dart method 
#   show that the area of any triangle is 
#   half of the area of the bounding box. 
#   The user should define the triangle by 
#   defining the corners as three points in space. 

import random
import math
for i in range(20):
    corner0 = 0
    cornerx = random.random()
    cornery = random.random()
    total = 0
    intri = 0
    print("triangle with sides x, y: " + str(cornerx) + ", " + str(cornery))
    for i in range(10000):
        x = random.random() 
        y = random.random() 
        if x <= cornerx and y <= cornery:
            total = total + 1
            d = math.sqrt(x*x * y*y)
            dy = cornery - x * (cornery / cornerx)
            dline = math.sqrt(dy*dy * x*x)
            if d <= dline:
                intri = intri + 1
    print(intri / total)

