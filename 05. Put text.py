#cv2.FONT_HERSHEY_SIMPLE: 보통 크기의 산 세리프(sans-serif) 글꼴
#cv2.FONT_HERSHEY_PLAIN: 작은 크기의 산 세리프 글꼴
#cv2.FONT_HERSHEY_SCRIPT_SIMPLEX: 필기체 스타일 글꼴
#cv2.FONT_HERSHEY_TRIPLEX: 보통 크기의 세리프 글꼴
#cv2.FONT_ITALIC: 기울임(이탤릭채)

import numpy as np
import cv2

img = np.zeros((480, 640, 3), dtype=np.uint8)

SCALE = 1 #크기
COLOR = (255,255,255) #흰색
THICKNESS = 1 #두께

cv2.putText(img, "Dong Dong", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindow()