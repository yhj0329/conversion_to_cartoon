import cv2
import numpy as np
# Load the image
img= cv2.imread('image.jpg')
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply median blur to reduce noise
gray = cv2.medianBlur(gray, 3)
# Detect edges using adaptive thresholding
good_edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 3)
bad_edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 11)
# Convert the image to color
good_color = cv2.bilateralFilter(img, 1, 300, 300)
bad_color = cv2.bilateralFilter(img, 9, 300, 300)
# Combine the color image with the edges mask
good_cartoon = cv2.bitwise_and(good_color, good_color, mask=good_edges)
bad_cartoon = cv2.bitwise_and(bad_color, bad_color, mask=bad_edges)

merge = np.hstack((good_cartoon, bad_cartoon))
# Display the cartoon image
cv2.imshow("Good Cartoon | Bad Cartoon", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()