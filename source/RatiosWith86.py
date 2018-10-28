import os
from statistics import mean
import math

def euc(x,y):
	d1 = (int(x[0])-int(x[1]))*(int(x[0])-int(x[1]))
	d2 = (int(y[0])-int(y[1]))*(int(y[0])-int(y[1]))
	d= math.sqrt(d1+d2)
	return d

def mid(x,y):
	j=(int(x[0])+int(y[0]))/2
	k = (int(x[1])+int(y[1]))/2
	ans= [j,k]
	return ans

images = os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\facial_landmarks\86\CF")
os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\facial_landmarks\86\CF")

ratios = []

for image in images:
	name = image.strip(".jpg")
	with open(image,'r') as fp:
		read_lines =fp.readlines()
		read_lines=[line.rstrip("\n") for line in read_lines]

	arry = [euc(read_lines[0],mid(read_lines[19],read_lines[5])), euc(read_lines[12],read_lines[67])]
	ratios.append(mean(arry))
	#ratios.append(mean(arry)/arry[0])
	#ratios.append(mean(arry)/arry[1])
	ratios.append(euc(read_lines[50],read_lines[54])/euc(read_lines[54],read_lines[42]))
	ratios.append(euc(read_lines[42],read_lines[46])/euc(read_lines[54],read_lines[42]))
	ratios.append(euc(read_lines[50],read_lines[17])/euc(read_lines[54],read_lines[42]))
	ratios.append(euc(read_lines[46],read_lines[5])/euc(read_lines[54],read_lines[42]))
	ratios.append(euc(read_lines[0],read_lines[11])/euc(read_lines[5],read_lines[17]))
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\ratios86\CF")
	file = open("{}_ratios86.txt".format(name),"w")
	for i in ratios:
		file.write(str(i))
		file.write("\n")
	del ratios[:]
	del read_lines[:]
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\facial_landmarks\86\CF")