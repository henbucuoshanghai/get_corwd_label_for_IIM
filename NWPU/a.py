import cv2
a=cv2.imread('0078.png')
b=cv2.imread('a.png')
print((a==b).all())

