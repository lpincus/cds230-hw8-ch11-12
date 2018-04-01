# Show that the DNA string contains only four letters. 

fname = open("ch12/dna.txt", "r")
fread = fname.read()
unique = set(fread)
fname.close()

for u in unique:
    print( u + " " + str(fread.count(u)))