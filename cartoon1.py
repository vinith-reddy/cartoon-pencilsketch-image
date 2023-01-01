import cv2
import sys
import os
import numpy as np
from PIL import Image
def display(f):
    img =cv2.imread(f.filename)
    path = r'C:\Users\chadu\OneDrive\Desktop\vinithdoc\projects\ProjChange\static'
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray =cv2.medianBlur(gray,5)
    edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    color=cv2.bilateralFilter(img,9,250,250)
    cartoon=cv2.bitwise_and(color,color,mask=edges)
    cv2.imwrite(os.path.join(path , 'cartoon.jpg'),cartoon)
    cv2.imwrite(os.path.join(path , 'image.jpg'),img)
    cv2.imwrite(os.path.join(path , 'gray.jpg'),gray)
    cv2.imwrite(os.path.join(path , 'edges.jpg'),edges)
    cv2.imwrite(os.path.join(path , 'color.jpg'),color)


    img_invert = cv2.bitwise_not(gray)
    gray_blur = cv2.GaussianBlur(gray,(25,25),0)
    pencil=cv2.divide(gray,gray_blur,scale=250.0)
    cv2.imwrite(os.path.join(path , 'gaussianblur.jpg'),gray_blur)
    cv2.imwrite(os.path.join(path , 'inverted.jpg'),img_invert)
    cv2.imwrite(os.path.join(path , 'pencil.jpg'),pencil)
cv2.waitKey(0)