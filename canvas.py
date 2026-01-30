import cv2
import numpy as np
from collections import deque

# Lower and upper HSV range for a color (tune for your marker)
lower_hsv = np.array([100, 150, 150])
upper_hsv = np.array([140, 255, 255])

# Store points
points = deque(maxlen=1024)

cap = cv2.VideoCapture(0)

# Canvas for drawing
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mask the chosen color
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Get largest contour and centroid
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if radius > 5:
            points.appendleft((int(x), int(y)))

    # Draw points
    for i in range(1, len(points)):
        if points[i - 1] and points[i]:
            cv2.line(canvas, points[i - 1], points[i], (255, 0, 0), 2)

    # Show frame and canvas
    cv2.imshow("Air Canvas", canvas)
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
