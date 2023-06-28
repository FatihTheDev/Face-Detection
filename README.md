# Face-Detection

his is a Python program that uses OpenCV library to detect faces in webcam rcordings. It is based on the Haar Cascade classifier, which is a machine learning technique that uses a cascade of simple features to identify objects in an image. The program uses the pre-trained models provided by OpenCV for face detection.

# Installation
To run this program, you need to have Python 3 and OpenCV installed on your system. You can install OpenCV using pip:
```
pip install opencv-python
```

You also need to download the cascade files for car and pedestrian detection from the following links and place them in the same folder as the program:

 [frontalface cascade file](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

# Usage
To use this program, you need to provide a video file as an argument.

The program will display the input file with bounding boxes around the detected cars and pedestrians. You can press the 'q' key to exit the program.

# Limitations
This program is not perfect and may have some limitations, such as:

It may not detect all cars and pedestrians in the input file, especially if they are partially occluded, too small, or too far away.

It may detect some false positives, such as other objects that look like cars or pedestrians, or shadows or reflections.

It may not work well in low-light or noisy conditions, or with different camera angles or perspectives.

# License
This program is licensed under the MIT License. See LICENSE for more details.
