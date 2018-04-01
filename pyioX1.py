# 1. 
dna_txt = open("ch12/dna.txt", "r").read()

#2. how many t in dna_txt
number_t = dna_txt.count("t")
print("number of ts ", str(number_t))

#2. t in 10-letter window
number_ts_list = []
print("num windows: " + str(len(dna_txt) / 10))
for i in range(int(len(dna_txt) / 10)):
    indx = i * 10
    number_ts = dna_txt[indx-10:indx].count("t")
    number_ts_list.append(number_ts)
print(number_ts_list)