import os 

names_ratios68 = os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\ratios68\CM")
names_ratios86 = os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\ratios86\CM")
names_eye = os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\eye_color\CM")
names_skin = os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\skin\CM")
i=0
names_list = []
for name in names_ratios68:
	name =name.strip(".jpg.txt")
	name = name.strip("ratiospoints")
	names_list.append(name)
print(names_list)
i=0
for name1 in names_list:
	if "ratiospoints{}.jpg.txt".format(name1) not in names_ratios68:
		continue
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\ratios68\CM")
	file = open("ratiospoints{}.jpg.txt".format(name1),"r")
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\All_features\CM")
	#f = open("CM_all_labels.txt","a")
	final =file.read().replace("\n",", ")
	#f.write(file.read())
	if name1+".txt_ratios86.txt" not in names_ratios86:
		continue
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\ratios86\CM")
	file = open("{}.txt_ratios86.txt".format(name1),"r")
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\All_features\CM")
	#f = open("CM_all_labels.txt","a")
	final +=file.read().replace("\n",", ")
	#f.write(file.read())
	if name1+"_eye_color.txt" not in names_eye:
		continue
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\eye_color\CM")
	file = open("{}_eye_color.txt".format(name1),"r")
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\All_features\CM")
	#f = open("CM_all_labels.txt","a")
	final +=file.read().replace("\n",", ")
	#f.write(file.read())
	if name1+".txt" not in names_skin:
		continue
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\skin\CM")
	file = open("{}.txt".format(name1),"r")
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\All_features\CM")
	f = open("CM_all_labels.txt","a")
	final +=file.read().replace("\n",", ")
	#f.write(file.read())
	print(name1)
	f.write(final)
	f.write(",")
	f.write("\n")
	i+=1
	
	f.close()
	file.close()    

'''
Failed Attempt
name1 = ""
i=0
for name1 in names_eye:
	if name1 in names_list:
		os.chdir(r"C:\\Users\\Win8.1\\source\repos\\Beauty_scorer\\parameters\\eye_color\\AM")
		file = open("{}".format(name1),"r")
		os.chdir(r"C:\\Users\\Win8.1\\source\repos\\Beauty_scorer\\parameters\\All_features\\AM")
		f = open("{}.txt".format(name1),"a")
		f.write(file.read())
		f.write("\n")
	i+=1
name1 = ""
names_list = []
for name in names_ratios68:
	name =name.strip(".jpg.txt")
	name = name.strip("ratiospoints")
	names_list.append(name)
i=0
for name1 in names_skin:
	if name1 in names_list:
		os.chdir(r"C:\\Users\\Win8.1\\source\repos\\Beauty_scorer\\parameters\\skin\\AM")
		file = open("{}".format(name1),"r")
		os.chdir(r"C:\\Users\\Win8.1\\source\repos\\Beauty_scorer\\parameters\\All_features\\AM")
		f = open("{}.txt".format(name1),"a")
		f.write(file.read())
		f.write("\n")
	i+=1
name1 = ""
names_list = []
for name in names_ratios68:
	name =name.strip(".jpg.txt")
	name = name.strip("ratiospoints")
	names_list.append(name)
i=0
for name1 in names_list:
	os.chdir(r"C:\\Users\\Win8.1\\source\repos\\Beauty_scorer\\parameters\ratios68\\AM")
	file = open("ratiospoints{}.jpg.txt".format(name1),"r")
	os.chdir(r"C:\\Users\\Win8.1\\source\repos\\Beauty_scorer\\parameters\\All_features\\AM")
	f = open("{}.txt".format(name1),"a")
	f.write(file.read())
	f.write("\n")
'''