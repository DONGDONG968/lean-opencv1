import cv2
cap = cv2.VideoCapture('image/video.mp4')

#코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

#프레임의 크기,FPS
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get (cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('out.avi', fourcc, fps, (width, height))
#저장 파일명, 코덱, FPS, 크기, (width, height)

while cap.isOpened(): # 동영상 파일이 올바로 열렸는지?
    ret, frame = cap.read() # ret : 성공여부, frame : 받아온 이미지(프레임)
    if not ret:
        print('더 이상 가져올 프레임이 없어요')
        break
    
    out.write(frame) #영상 데이터만 저장(소리x)
    cv2.imshow('video', frame)

    if cv2.waitKey(25) == ord('q'):
        print('사용자 입력에 의해 종료 합니다')
        break

out.release()
cap.release() # 자원 해제
cv2.destroyAllWindow() 