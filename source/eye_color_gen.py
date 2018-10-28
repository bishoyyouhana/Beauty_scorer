import os 
import cv2
import numpy
from PIL import Image

images = os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_images\CM")
for image in images:
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\facial_landmarks\86\CM")
	name = image.rstrip(".jpg")
	with open("{}.txt".format(name),"r") as fp:
		read_lines = fp.readlines()
		read_lines = [line.rstrip('\n') for line in read_lines]
	pixel_left = read_lines[58]
	pixel_right = read_lines[59]
	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_images\CM")
	im =Image.open(image)
	rgb_im = im.convert("RGB")
	pixel_left = pixel_left.split(" ")
	pixel_right = pixel_right.split(" ")
	r_left, g_left, b_left= rgb_im.getpixel((int(float(pixel_left[0])),int(float(pixel_left[1]))))
	r_right, g_right, b_right= rgb_im.getpixel((int(float(pixel_right[0])),int(float(pixel_right[1]))))
	r=(r_left + r_right)/2
	g=(g_right+g_left)/2
	b =(b_right+b_left)/2
	color=[r,g,b]

	os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\eye_color\CM")
	f = open("{}_eye_color.txt".format(name), "w")
	for p in color:
		f.write(str(p))
		f.write("\n")