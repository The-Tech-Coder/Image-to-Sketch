import cv2

image = cv2.imread("lizzie.jpg")
# This will show the main Image
# cv2.imshow("img", image)
# cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# This will show the Greyscale Image
# cv2.imshow("New img", gray_image)
# cv2.waitKey(0)

inverted_image = 255 - gray_image
# This will show the Inverted Greyscale Image
# cv2.imshow("Inverted", inverted_image)
# cv2.waitKey(0)

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
# bluring the image by using the Gaussian Function in OpenCV

inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
# This will invert the blurred image
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

# Both the original image and the pencil sketch
# cv2.imshow("original image", image)
# cv2.imshow("pencil sketch", pencil_sketch)
# cv2.waitKey(0)
