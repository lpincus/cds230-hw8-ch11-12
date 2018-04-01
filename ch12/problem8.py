# 8. What is the most common
#   word in Romeo and Juliet 
#   that is at least 5 letters long?

romeo_and_juiet = open("ch12/romeo-and-juliet.txt", "r").read()
word_list = romeo_and_juiet.split(" ")
five_letter_list = []
for word in word_list:
    if len(word) >= 5:
        five_letter_list.append(word)
repeated_word = ""
repeated_times = 0
five_letter_set = set(five_letter_list)
for word in five_letter_set:
    this_times = five_letter_list.count(word)
    if this_times > repeated_times:
        repeated_times = this_times
        repeated_word = word

print("the most repeated word is: word, times " + repeated_word + ", " + str(repeated_times))