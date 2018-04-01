# 4. In Romeo and Juliet 
# retrieve all of the capitalized words 
# that do not start a sentence. 
# Use set and list to remove duplicates from this list.

import re
romeo_and_juliet = open("ch12/romeo-and-juliet.txt", "r").read()
pattern = r".*[a-z] ([A-Z][a-z]*)"
complete_list = re.findall(pattern, romeo_and_juliet)
print(set(complete_list))
