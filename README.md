Air Canvas is an interactive computer vision project developed using Python that allows users to draw on a virtual canvas by moving a colored marker or fingertip in front of a webcam. The application captures live video, tracks movement using OpenCV, and renders the drawing in real time without using traditional input devices such as a mouse or touchscreen.

Features

Real-time drawing using webcam input
Color-based object tracking
Virtual canvas for freehand drawing
Live video processing using OpenCV
Optional visualization using Matplotlib

Technologies Used

Python
OpenCV
NumPy
Matplotlib

Project Structure

air-canvas/
air_canvas.py
README.md

Prerequisites

Python 3.x
Webcam
pip package manager

Required Libraries

Install the required libraries using the following command:

pip install opencv-python numpy matplotlib

How the Project Works

The webcam captures live video frames which are converted from BGR to HSV color space. A specific color range is detected to identify the drawing object. The position of the detected object is tracked frame by frame and stored as coordinates. These coordinates are connected to form continuous lines on a virtual canvas, creating a drawing effect.

How to Run the Project

Clone or download the project
Open a terminal in the project directory
Run the Python file using the command:

python air_canvas.py


Move a colored object in front of the webcam to start drawing
Press the 'q' key to exit the application

Applications

Virtual drawing and sketching
Gesture-based interaction systems
Computer vision learning projects
Human-computer interaction demonstrations

Learning Outcomes

Understanding real-time video processing
Color detection and tracking using OpenCV
Working with contours and coordinates
Basic computer vision concepts
Interactive application development

Future Enhancements

Hand gesture recognition using MediaPipe
Multiple color selection
Eraser functionality
Save drawings as image files
