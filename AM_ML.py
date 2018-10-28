import numpy as np
from sklearn import decomposition
from sklearn import linear_model
from numpy import array
'''
with open(r'C:\\Users\\Win8.1\\source\repos\\Beauty_scorer\\parameters\\All_features\\AM\\AM_all_labels.txt',"r") as f:
	file = f.readlines()
	file= file.replace(",,","--")
	for line in file:
		line.replace(",","\n")
	f= open(r'C:\\Users\\Win8.1\\source\repos\\Beauty_scorer\\parameters\\All_features\\AM\\AM_all_labels.txt',"w")
	print(type(file))
	f.write(file)
'''
j=0
i=0
f =  open(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\All_features\AM\AM_all_labels.txt","r")
features = f.readlines()
for line in features:
	line= line.split(",")
	line.remove("\n")
	'''
	for someline in line:
		line[j] = float(someline)
		j+=1
	'''
	features[i] = line
	i+=1
print(features)
features = np.asarray(features, dtype=np.float32)
#features = np.loadtxt(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\All_features\AM\AM_all_labels.txt", delimiter=',')
#features = np.loadtxt(r'C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\All_features\AM\AM_all_labels.txt', delimiter=',,')
i=0
f =  open(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_ratings\AM_ratings.txt","r")
ratings = f.readlines()
for line in ratings:
	line= line.strip(",")
	line= line.strip("\n")
	ratings[i] = int(line)
	i+=1
#print(ratings)
ratings = np.asarray(ratings, dtype=np.float32)
#ratings = np.loadtxt(r'C:\Users\Win8.1\source\repos\Beauty_scorer\training_ratings\AM_ratings.txt', delimiter=',')
i=0
#img_test= np.loadtxt(r"C:\Users\Win8.1\Desktop\testing_img\AM\features",delimiter=',,')
f =  open(r"C:\Users\Win8.1\Desktop\testing_img\AM\features\features.txt","r")
img_test = f.read()
img_test = img_test.replace("\n"," ")
img_test = img_test.split(",,")
while i<len(img_test):
	img_test[i] = img_test[i].split(" ")
	if i != 0:
		img_test[i] = img_test[i].remove('')
	i+=1
img_test = img_test.remove(None)
'''
for line in img_test:
	line= line.strip("\n")
	line= line.split(",,")
	final.append
	i+=1
'''
print(img_test)
img_test = np.asarray(img_test, dtype=np.float32)
i=0
#img_test_ratings= np.loadtxt(r"C:\Users\Win8.1\Desktop\testing_img\AM\ratings",delimiter=',,')
f =  open(r"C:\Users\Win8.1\Desktop\testing_img\AM\ratings\raaaatings.txt","r")
img_test_ratings = f.readlines()
for line in img_test_ratings:
	line= line.strip(",,")
	line= line.strip("\n")
	img_test_ratings[i] = line
	i+=1
#print(img_test_ratings)
img_test_ratings = np.asarray(img_test_ratings, dtype=np.float32)

pca = decomposition.PCA(n_components=35)
pca.fit(features)
features = pca.transform(features)
#img_test = pca.transform(img_test)

regr = linear_model.LinearRegression()
regr.fit(features, ratings)
ratings_predict = regr.predict(img_test)

corr = np.corrcoef(ratings_predict, img_test_ratings)[0, 1]

print(corr)