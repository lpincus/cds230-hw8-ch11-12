# 2. In the DNA string there are regions that have a repeating letter. What is the letter and length of the longest repeating region? 

fname = open("ch12/dna.txt", "r")
fread = fname.read()
long_letter = 0
long_number = 0
last_letter = 0
this_number = 0

for i in range(len(fread)):
    letter = fread[i]
    if letter == last_letter: # it matches
        this_number = this_number + 1
    else: # new letter 
        if this_number > long_number: # new longest 
            long_number = this_number
            long_letter = last_letter
        this_number = 0
        last_letter = letter

    if i == 0:
        last_letter = letter
        long_letter = letter

print("longest letter, repeats: " + long_letter + ", " + str(long_number))
    
    
        


