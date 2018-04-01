#6. Create a list of 10 data points 
#   in the form of (x, y). 
#   The values of these points can be randomly assigned. 
#   Write a Python script in which 
#   both the x and y values are used as indexes in the for loop. 
#   Print the values for each iteration. 
import random
xy =  [(random.random(), random.random()) for i in range(10)]
for x, y in xy:
    print("(" + str(x) + "," + str(y) + ")")

