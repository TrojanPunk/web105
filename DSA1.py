#Reversing the order of lines. We will use the above text file as input.
f1 = open("gfg.txt", "w")

with open("gfg1.txt", "r") as gfglocal:
	data = gfglocal.read()

reverse = data[::-1]

f1.write(reverse)

f1.close()

f2 = open("gfg2.txt", "w")

with open("gfg1.txt", "r") as gfglocal:
	data = gfglocal.readlines()

reverse1 = data[::-1]

f2.writelines(reverse1)

f2.close()

