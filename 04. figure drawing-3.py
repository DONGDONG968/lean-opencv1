### 직선
### 직선의 종류
### 1. cv2.LINE_4: 상하좌우 4 방향으로 연결된 선 
### 2. cv2.LINE_8: 대각선을 포함한 8 방향으로 연결된 선(기본값)
### 3. cv2.LINE_AA: 부드러운 선

import cv2
import numpy as np

# 세로 480 X 가로 640, Channel 3 (RGB) 에 해당하는 스케치북 만들기
img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 255, 255) # 색깔, BGR : Yellow ==> Blue(0), Green(255), Red(255) 초록색max + 빨간색max = Yellow
THICKNESS = 3 #두께

# line ==> 직선을 그린다
# img ==> 빈 스케치북에
# (img, (50,100), (400,50)) ==> 빈 스케치북의 (50,100) 에서 (400,50) 까지 직선을 그린다
# (img, (50,100), (400,50), COLOR) ==> 색깔은 Yellow 로 한다
# (img, (50,100), (400,50), COLOR, THICKNESS) ==> 두께는 3으로 한다
# (img, (50,100), (400,50), COLOR, THICKNESS, CV2.LINE_8) ==> 직선의 종류는 '대각선을 포함한 8 방향을 연결된 선'으로 한다
cv2.line(img, (50,100), (400,50), COLOR, THICKNESS, cv2.LINE_8)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindow()
