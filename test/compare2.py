import cv2
from PIL import Image
import numpy as np
#from resizeimage import resizeimage

def check(img1,img2):
    res=cv2.absdiff(img1,img2)
    res=res.astype(np.uint8)
    percentage=(np.count_nonzero(res)*100)/res.size
    print(percentage)

def resize1(img1,img2):
    r1=cv2.resize(img1,(300,100))  
    r2=cv2.resize(img2,(300,100))
    check(r1,r2)
    

img=cv2.imread('temp.png')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=cv2.imread('cpy.png')
img3=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

resize1(img1,img3)


#check(img1,img3)
