"""
Docstring for opencv-mocv.M1_exercises
This file contains the code for all exercises of "Mastering OpenCV with Python" course, Module 1

Created on 01/01/2026
Author: marcos perez
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

#========
#01-01
#========
# Read the image ('Apollo-11-launch.jpg') using OpenCV imread() as a grayscale image.
img_bgr = cv2.imread("./module01/Apollo-11-launch.jpg", cv2.IMREAD_GRAYSCALE)

# Print the image width and height.
print("image width: ", img_bgr.shape[1])
print("image height: ", img_bgr.shape[0])
print("pixels format: ", img_bgr.dtype)

# Display the image using matplotlib imshow().
plt.figure(0)
plt.imshow(img_bgr, cmap = 'gray')
plt.title("Apollo 11 Launch", fontsize = 12)
plt.show()

# Save the image as a PNG file using OpenCV imwrite().
cv2.imwrite("Apollo-11-launch.png", img_bgr)

#========
#01-02
#========
# Read the saved image above ('Emerald_Lakes_New_Zealand.jpg') as a color image.
img_bgr = cv2.imread("./module01/Emerald_Lakes_New_Zealand.jpg", cv2.IMREAD_COLOR)

# Print the image shape.
print("BGR Image shape: ", img_bgr.shape)

# Convert the image to grayscale using cv2.cvtColor().
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Print the image shape.
print("grayscale image shape: ", img_gray.shape)

# Display the image using matplotlib imshow()
plt.figure(figsize = [10, 10])
plt.imshow(img_gray, cmap = 'gray')
plt.show()

#========
#01-03
#========
img = cv2.imread("./module01/New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
print("image shape: ", img.shape)
plt.figure(figsize=[3,3])
plt.imshow(img[:,:,::-1])   #print RGB format (image is BGR)
plt.show()

# Crop the image to extract the region around the sale boat.
img_crop = img[205:271,340:391,:]
print("shape of cropped image: ", img_crop.shape)

# Resize the image up by a factor of 2x.
img_crop_resize = cv2.resize(img_crop, None, fx=2, fy=2)
print("shape of cropped,resized image: ", img_crop_resize.shape)

# Flip the cropped/resized image horizontally.
img_crop_resize_flip = cv2.flip(img_crop_resize, 1)

# Display the final result.
plt.figure(1,figsize = [5, 5])
plt.imshow(img_crop_resize_flip[:,:,::-1])
plt.show()

#========
#01-04
#========
# Read in the image ('Apollo-11-launch.jpg').
img = cv2.imread("./module01/Apollo-11-launch.jpg", cv2.IMREAD_COLOR)  #--> imread_color to allow me to put annotations in colour.

# Add the following text to the dark area at the bottom of the image (centered on the image):
# 'Apollo 11 Saturn V Launch, July 16, 1969'.
text = 'Apollo 11 Saturn V Launch, July 16, 1969' 
font_face = cv2.FONT_HERSHEY_PLAIN 
green = (0,255,0)     #bgr
magenta = (255,0,255) #bgr

# YOUR CODE HERE: use putText()
img_text = cv2.putText(img, text, (300,700), font_face, fontScale = 2, color=green, lineType = cv2.LINE_AA)

# Draw a magenta rectangle that encompasses the launch tower and the rocket.
img_text_rectangle = cv2.rectangle(img_text, (500,100),(700,600), magenta, thickness=3, lineType = cv2.LINE_8)

# Display the final annotated image
# plt.figure(figsize=[12, 12])
plt.figure(figsize = [8,8])
plt.imshow(img_text_rectangle)
plt.show()

