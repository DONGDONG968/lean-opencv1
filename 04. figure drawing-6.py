### 직선
### 직선의 종류
### 1. cv2.LINE_4: 상하좌우 4 방향으로 연결된 선 
### 2. cv2.LINE_8: 대각선을 포함한 8 방향으로 연결된 선(기본값)
### 3. cv2.LINE_AA: 부드러운 선

import cv2
import numpy as np

# 세로 480 X 가로 640, Channel 3 (RGB) 에 해당하는 스케치북 만들기
img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 0, 255) # 색깔, BGR 빨간색
THICKNESS = 3 #두께

pts1 = np.array([[100, 100], [200, 100], [100, 200]])
cv2.polylines(img, [pts1], True, COLOR, THICKNESS, cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destoryAllWindows()