import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

# img(이미지파일)의 [세로(100:200) : 가로(200:300)] 부분을 흰색(255,2 55, 255)으로 변경 
img[100:200, 200:300] = (255, 255, 255) 

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindow()