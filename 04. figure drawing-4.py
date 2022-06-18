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
RADIUS = 50 # 반지름
THICKNESS = 10 #두께

# circle ==> 원을 그린다
# img ==> 빈 스케치북에
# (img, (200,100)) ==> 빈 스케치북에 원을 그릴 중심점(200,100)
# (img, (50,100), (400,50), COLOR) ==> 색깔은 Yellow 로 한다
# (img, (50,100), (400,50), COLOR, THICKNESS) ==> 두께는 10으로 한다
# (img, (200,100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA) ==> 선의 종류는 '부드러운 선'으로 한다
cv2.circle(img, (200,100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA)

# THICKNESS 대신 cv2.FILLED를 넣어 꽉찬 원을 그린다
cv2.circle(img, (400,100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindow()
