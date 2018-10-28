import os 

images = os.listdir(r"C:\Users\Win8.1\source\repos\Face_stuff\SCUT-FBP5500_v2\Images")

os.chdir(r"C:\Users\Win8.1\source\repos\Face_stuff")

f= open("images_names.txt","a")
for image in images:
	f.write("\"{}\"".format(image))
	f.write(", ")
