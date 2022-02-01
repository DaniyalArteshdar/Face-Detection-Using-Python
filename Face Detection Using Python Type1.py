# Coded by Daniyal Arteshdar

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
mpFaceDetection = mpFaceDetection.FaceDetection()

while True :
    success,img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = mpFaceDetection.process(imgRGB)
    print(results)

    if results.detections :
        for id,detection in enumerate(results.detections):
            mpDraw.draw_detection(img,detection)

            print(id, detection)
            print(detection.score)
            print(detection.location_data.RELATIVE_BOUNDING_BOX)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS : {int(fps)}', (20, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
