def getArryPx(contours,image):
    im =Image.open(image)
    rgb_im = im.convert("RGB")
    x =0
    y=0
    #lst_px_values =[]
    R1=[]
    G1=[]
    B1=[]
    for i in range(len(contours)):
        #cimg=numpy.zeros_like(image)
        img=cv2.imread(image)
        cv2.drawContours(img, contours, i, color=255, thickness=-1)
        pts=numpy.where(img==255)
        #lst_px_values.append(img[pts[0], pts[1]])
        x,y=pts[0], pts[1]
        rgb = im.getpixel((pts[1]))
        R1[i]=rgb[0]
        G1[i]=rgb[1]
        B1[i]=rgb[2]                                               
        i +=1
        return R1, G1, B1