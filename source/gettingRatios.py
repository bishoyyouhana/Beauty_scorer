import math
import os

def euc(x,y):
	d1 = (x[0]-x[1])*(x[0]-x[1])
	d2 = (y[0]-y[1])*(y[0]-y[1])
	d= math.sqrt(d1+d2)
	return d
l=0
files=os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\facial_landmarks\68\AM")
ratios = []
coordinates = []
for file in files:
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\facial_landmarks\68\AM")
	f = open(file,"r")
	coords= f.readlines()
	for coord in  coords:
		coord= coord.rstrip('\n')
		coord= coord.rstrip('\r')
		split = coord.split(",")
		x= int(float(split[0]))
		y= int(float(split[1]))
		coordinates.append([x,y])
	ratios.append(euc(coordinates[13], coordinates[17])/euc(coordinates[9],coordinates[13]))
	ratios.append(euc(coordinates[1], coordinates[5])/euc(coordinates[5],coordinates[9]))
	ratios.append(ratios[0]/ratios[1])
	ratios.append(euc(coordinates[52], coordinates[53])/euc(coordinates[54],coordinates[55]))
	ratios.append(euc(coordinates[51], coordinates[52])/euc(coordinates[49],coordinates[50]))	

	ratios.append(ratios[3]/ratios[4])
	ratios.append(euc(coordinates[55], coordinates[56])/euc(coordinates[57],coordinates[58]))
	ratios.append(euc(coordinates[49], coordinates[60])/euc(coordinates[58],coordinates[59]))
	ratios.append(ratios[6]/ratios[7]) # 8 
	ratios.append(euc(coordinates[28], coordinates[29])/euc(coordinates[30],coordinates[31])) #9
	ratios.append(euc(coordinates[36], coordinates[35])/euc(coordinates[34],coordinates[35]))#10
	ratios.append(euc(coordinates[32], coordinates[33])/euc(coordinates[33],coordinates[34])) #11
	ratios.append(ratios[10]/ratios[11])
	ratios.append(ratios[9]/ratios[12])#13	

	ratios.append(euc(coordinates[40], coordinates[37])/euc(coordinates[42],coordinates[38]))#14
	ratios.append(euc(coordinates[46], coordinates[43])/euc(coordinates[44],coordinates[48]))#15
	ratios.append(ratios[14]/ratios[15])
	ratios.append(euc(coordinates[39], coordinates[42])/euc(coordinates[38],coordinates[41]))#17
	ratios.append(euc(coordinates[45], coordinates[48])/euc(coordinates[44],coordinates[47]))#18
	ratios.append(ratios[17]/ratios[18])
	ratios.append(ratios[16]/ratios[19])
	ratios.append(ratios[8]/ratios[5])
	
	del coordinates[:]
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\ratios68\AM")
	r = open("ratios{}".format(file),"w")
	for j in ratios:
		r.write(str(j))
		r.write("\n")	
	del ratios[:]