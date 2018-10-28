import cv2
import numpy
import os
from PIL import Image
import face_recognition
import math
import sys 
from collections import namedtuple
# Constants for finding range of skin color in YCrCb

def SaveBook(book):
    f = open("BookData.csv","a+")
    f.write(book[0] + ',' + book[1] + ',' + book[2] + ',' + book[3] + '\n')
    f.close()
def getArryPx(contours,image):
    img=cv2.imread(image)
    im =Image.open(image)
    rgb_im = im.convert("RGB")
    mask = numpy.zeros(img.shape[:2], dtype="uint8")
    x =0
    y=0
    #lst_px_values =[]
    R1=[]
    G1=[]
    B1=[]
    #for i in range(len(contours)):
        #cimg=numpy.zeros_like(img)
    cv2.drawContours(mask, contours, -1, color=255, thickness=-1)
    mean = cv2.mean(img, mask=mask)[:3]
    R1, G1, B1= mean[0],mean[1], mean[2]
    #pts=numpy.where(cimg==255)
    #lst_px_values.append(img[pts[0], pts[1]])
    return R1, G1, B1

def SumPx(R,G,B):
    j=0
    TR = 0
    TG = 0
    TB =0
    for r in R:
        TR += r
        j+=1
    j=0
    for g in G:
        TG += g
        j+=1
    for b in B:
        TB += b
        j+=1
    return TR, TG, TB
def AvgPxVal(R,G,B):
    j=0
    TR =0
    TG =0
    TB =0
    for r in R:
        TR += r
        j+=1
    AvgR = TR/j 
    j=0
    for g in G:
        TG += g
        j+=1
    AvgG = TG/j 
    j=0
    for b in B:
        TB += b
        j+=1
    AvgB = TB/j 
    return AvgR, AvgG, AvgB

def STDPxVal(R,G,B):
    totalr = 0
    totalb = 0
    totalg = 0
    r,g,b= AvgPxVal(R,G,B)
    rsum, gsum,bsum= SumPx(R,G,B)
    for i in range(len(R)):
        bumr = (i-r)*(i-r)
        totalr += bumr
    for i in range(len(G)):
        bumg = (i-g)*(i-g)
        totalg += bumg
    for i in range(len(B)):
        bumb = (i-b)*(i-b)
        totalb += bumb
    STDR= math.sqrt(totalr/len(R))
    STDG= math.sqrt(totalg/len(G))
    STDB= math.sqrt(totalb/len(B))
    return STDR,STDG,STDB
min_YCrCb = numpy.array([109,42,15],numpy.uint8)
max_YCrCb = numpy.array([240,191,188],numpy.uint8)
i=0
#filenames=os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_images\CM")
os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_images\CM")

j=0
filenames=os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_images\CM")
for sourceImage in filenames:
    image=cv2.imread(sourceImage)

    # Convert image to YCrCb- most reliable color space i found 
    imageYCrCb = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)

    # Find region with skin tone in YCrCb image
    skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)
    
    # Do contour detection on skin region
    skinRegion, contours, hierarchy = cv2.findContours(skinRegion ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.RETR_EXTERNAL,
    # Draw the contour on the source image
    for a, c in enumerate(contours):
        area = cv2.contourArea(c)
        if area > 200:
            cv2.drawContours(image, contours, a, (0, 255, 0), 3)

    # Display the source image
    '''
    pil_image= Image.open(skinRegion)
    pil_image.save(i)
    '''
    #cv2.imshow('Output',skinRegion)
    name= str(j)+ ".jpg"
    #cv2.imwrite(name, image)
    R,G,B=getArryPx(contours,sourceImage)
    #Avgr,Avgg,Avgb = AvgPxVal(R,G,B)
    #stdr,stdg,stdb= STDPxVal(R,G,B)
    print("average value of R:{} G:{} B:{}".format(R,G,B))
    #print("STD value of R:{} G:{} B:{}".format(R,G,B))
    
    #book=[name, Avgr,Avgg,Avgb, stdr,stdg,stdb]
    os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\parameters\skin\CM")
    sourceImage = sourceImage.rstrip(".jpg")
    f =open("{}.txt".format(sourceImage),"w")
    avgname = str(int(R))+"\n"+str(int(G))+"\n"+str(int(B))
    #stdname = str(stdr)+" "+str(stdg)+" "+str(stdb)
    f.write(avgname)
    #f.write("\n")
    #f.write(stdname)
    os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_images\CM")
    f.close()
    #SaveBook(book)
    #cv2.waitKey()
    
    j+=1
#print(sourceImage)
# Check for user input to close program
#keyPressed = cv2.waitKey(2)  wait 2 millisecond in each iteration of while loop
# Close window and camera after exiting the while loop
cv2.destroyWindow('Output')
#videoFrame.release()
input("press enter to exit")
