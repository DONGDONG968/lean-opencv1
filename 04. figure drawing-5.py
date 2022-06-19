### 직선
### 직선의 종류
### 1. cv2.LINE_4: 상하좌우 4 방향으로 연결된 선 
### 2. cv2.LINE_8: 대각선을 포함한 8 방향으로 연결된 선(기본값)
### 3. cv2.LINE_AA: 부드러운 선

import cv2
import numpy as np

# 세로 480 X 가로 640, Channel 3 (RGB) 에 해당하는 스케치북 만들기
img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 255, 0) # 색깔, BGR : Green ==> Blue(0), Green(255), Red(0) 초록색max
THICKNESS = 3 #두께

# 사각형을 그릴 시작점(100,100) 에서 끝점 
cv2.rectangle(img, (100,100), (200,200), COLOR, THICKNESS) # 속이 빈 사각형

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destoryAllWindows()