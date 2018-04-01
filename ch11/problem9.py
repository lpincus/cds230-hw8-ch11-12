# 9. 
# Section 11.3.4 uses a circle 
# that is inside of a square. 
# Using the random dart method 
# compute the area of a square 
# that is inside of a unit circle 
# with all four corners touching 
# the circle.

import math
import random
diagonal = 2
side = math.sqrt(2)
total = 0
insquare = 0
for i in range(1000000):
    x = random.random() * 2
    y = random.random() * 2
    total = total + 1
    if x <= side and y <= side:
        insquare = insquare + 1
print(insquare / float(total))