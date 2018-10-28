import numpy as np
from sklearn import decomposition
from numpy import array

with open(r'C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\All_features\AM\AM_all_labels.txt',"w") as f:
	file = f.readlines()
	file= file.replace(",,","--")
	file = file.replace(",","\n")
	f.write(file)
    features = np.loadtxt(r'C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\All_features\AM\AM_all_labels.txt', delimiter="--")

#features = np.loadtxt(r'C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\All_features\AM\AM_all_labels.txt', delimiter=',,')
ratings = np.loadtxt(r'C:\Users\Win8.1\source\repos\Beauty_scorer\training_ratings\AM_ratings.txt', delimiter=',,')

img_test= np.loadtxt(r"C:\Users\Win8.1\Desktop\testing_img\AM\features",delimiter=',,')
img_test_ratings= np.loadtxt(r"C:\Users\Win8.1\Desktop\testing_img\AM\ratings",delimiter=',,')

pca = decomposition.PCA(n_components=20)
pca.fit(features)
features = pca.transform(features)
img_test = pca.transform(img_test)

regr = linear_model.LinearRegression()
regr.fit(features, ratings)
ratings_predict = regr.predict(img_test)

corr = np.corrcoef(ratings_predict, img_test_ratings)[0, 1]

print(corr)