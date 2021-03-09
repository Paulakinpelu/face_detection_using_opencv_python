import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input video
video=cv2.VideoCapture('video1.mp4')

while video.isopened():
    _, img = video.read
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

    #Display the output
    cv2.imshow('img', img)
    cv2.waitKey()

video.release()