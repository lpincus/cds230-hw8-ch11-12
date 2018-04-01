# 7. What is the largest distance 
#   (number of characters) 
#   between two consecutive instances 
#   of the word “Juliet”. 
# (The previous problem will be of assistance.) 

romeo_and_juiet = open("ch12/romeo-and-juliet.txt", "r").read()
word_list = romeo_and_juiet.split(" ")
index_list = []
i = 0
for word in word_list:
    if word.lower() == "juliet":
        index_list.append(i)
    i = i + 1
distnace_list = []
for i in range(1, len(index_list)):
    distnace_list.append(index_list[i] - index_list[i-1])
print(max(distnace_list))