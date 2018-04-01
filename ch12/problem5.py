# 5. 
# Does the phrase “Juliet and Romeo” 
#   exist in the play?

romeo_and_juliet = open("ch12/romeo-and-juliet.txt", "r").read()
if romeo_and_juliet.count("Juliet and Romeo") > 0:
    print("yes")
else: 
    print("no")