import cv2
framewidth = 400
frameheight = 100
cap = cv2.VideoCapture(0)
# cap.set(3,frameheight)
# cap.set(4,framewidth)
while True:
   sucess ,img = cap.read()
   img = cv2.resize(img,(framewidth,frameheight))
   cv2.imshow("video", img)
   if cv2.waitKey(1) & 0xFF == ord("q"):
      break
cv2.waitKey()