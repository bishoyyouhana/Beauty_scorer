import pandas as pd 
import os

file= pd.ExcelFile(r"C:\Users\Win8.1\source\repos\Face_stuff\SCUT-FBP5500_v2\All_Ratings.xlsx")
names_ratios68 = os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\ratios68\AM")

names_list = []
for name in names_ratios68:
	name =name.strip(".jpg.txt")
	name = name.strip("ratiospoints")
	name +=".jpg"
	names_list.append(name)

sheet_names = file.sheet_names

df1 = file.parse(sheet_names[1])
df2 = file.parse(sheet_names[2])
df3 = file.parse(sheet_names[3])
df4 = file.parse(sheet_names[4])

df1_ratings=0
df2_ratings=0
df3_ratings=0
df4_ratings=0

df1_finals=[]
df2_finals=[]
df3_finals=[]
df4_finals=[]

i=0
j=0
while j<750:
	i=0
	df1_ratings=0
	while i<60:
		df1_ratings += int(df1["Rating"][i+(j*60)])
		i+=1
	if df1["Filename"][j] != names_list[j]:
		continue 
	df1_finals.append(df1_ratings/60)
	j+=1
	print(j)
i=0
j=0
while j<750:
	i=0
	df2_ratings=0
	while i<60:
		df2_ratings += int(df2["Rating"][i+(j*60)])
		i+=1
	if df1["Filename"][j] != names_list[j]:
		continue 
	df2_finals.append(df2_ratings/60)
	j+=1
	print(j)
i=0
j=0
while j<2000:
	i=0
	df3_ratings=0
	while i<60:
		df3_ratings += int(df3["Rating"][i+(j*60)])
		i+=1
	if df1["Filename"][j] != names_list[j]:
		continue 
	df3_finals.append(df3_ratings/60)
	j+=1
	print(j)
i=0
j=0
while j<2000:
	i=0
	df4_ratings=0
	while i<60:
		df4_ratings += int(df4["Rating"][i+(j*60)])
		i+=1
	if df1["Filename"][j] != names_list[j]:
		continue 
	df4_finals.append(df4_ratings/60)
	j+=1
	print(j)
print(df1_finals)
print("some space")
print(df2_finals)
print("some space")
print(df3_finals)
print("some space")
print(df4_finals)

os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_ratings")

f = open("CF_ratings.txt","w")
for every_rat1 in df1_finals:
	f.write(str(int(every_rat1)))
	f.write("\n")
	f.write(",")

f = open("CM_ratings.txt","w")
for every_rat2 in df2_finals:
	f.write(str(int(every_rat2)))
	f.write("\n")
	f.write(",")

f = open("AF_ratings.txt","w")
for every_rat3 in df3_finals:
	f.write(str(int(every_rat3)))
	f.write("\n")
	f.write(",")

f = open("AM_ratings.txt","w")
for every_rat4 in df4_finals:
	f.write(str(int(every_rat4)))
	f.write("\n")
	f.write(",")

f.close()