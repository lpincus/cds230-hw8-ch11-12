# 6. Return a list 
#   of all of the locations 
#   of the word “Juliet”.

romeo_and_juiet = open("ch12/romeo-and-juliet.txt", "r").read()
word_list = romeo_and_juiet.split(" ")
index_list = []
i = 0
for word in word_list:
    if word.lower() == "juliet":
        index_list.append(i)
    i = i + 1
print("juliet is at these word numbers: ")
print(index_list)