import cv2
import numpy as np
import os
from PIL import Image

os.chdir(r"C:\Users\Win8.1\source\repos\Face_stuff\skin_test")
contours,_ = cv2.findContours(img, cv2.RETR_LIST, cv2.cv.CV_CHAIN_APPROX_NONE)
image="face -12.jpg"
getArryPx(contours,image)
def getArryPx(contours,image):
	im = Image.open(image)
	rgb_im = im.convert('RGB')
# Initialize empty list
	lst_intensities=[]
	R=[]
	G=[]
	B=[]
# For each list of contour points...
	for i in range(len(contours)):
	    # Create a mask image that contains the contour filled in
	    cimg = np.zeros_like(img)
	    cv2.drawContours(cimg, contours, i, color=255, thickness=-1)

    # Access the image pixels and create a 1D numpy array then add to list
	    pts = np.where(cimg == 255)
	    lst_intensities.append(img[pts[0], pts[1]])
		r, g, b = rgb_im.getpixel((img[pts[0], pts[1]])
		R[i]=r
		G[i]=g
		B[i]=b
		i+=1
		return R, G, B

