import os

names_list = []
names_ratios68 = os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\ratios68\AF")

for name in names_ratios68:
	name =name.strip(".jpg.txt")
	name = name.strip("ratiospoints")
	name +=".jpg"
	names_list.append(name)
print("stuff")
df1_ratings = 0
df1_finals=[]
ratings=[] 
names = []

file = open("ratings.txt","r")
g=0
with file as fp:
    read_lines = fp.readlines()
    read_lines = [line.rstrip('\n') for line in read_lines]
print(read_lines)
for line2 in read_lines:
	test = line2.split("\t")
	names.append(test[0])
	ratings.append(test[1])
	names[g] = names[g].strip(" ")
	ratings[g]=ratings[g].strip(" ")
	g+=1
i=0
j=0
while j<2000:
	i=0
	df1_ratings=0
	while i<60:
		df1_ratings += int(ratings[1+j*60])
		i+=1
	if names[j+2] not in names_list:
		continue 
	df1_finals.append(df1_ratings/60)
	j+=1
	print(j)
os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_ratings")
f = open("AF_ratings.txt","w")
for every_rat1 in df1_finals:
	f.write(str(int(every_rat1)))
	f.write("\n")
	f.write(",")

f.close()
