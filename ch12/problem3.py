# 3. How many ’ATG’s are in the DNA string?
# Kinser, Jason. 
#   Computational Methods for Bioinformatics: 
#   Python 3.4 (Page 201).  . Kindle Edition. 

dna_string = open("ch12/dna.txt", "r").read()
print(dna_string.count("atg"))
