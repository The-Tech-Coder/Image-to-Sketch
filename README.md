# Image-to-Sketch
Python Code that converts an Image into a Pencil Sketch

Explanation: <br>we need to read the image in RBG format and then convert it to a grayscale image.
This will turn an image into a classic black and white photo.
Then the next thing to do is invert the grayscale image also called negative image,
this will be our inverted grayscale image. Inversion can be used to enhance details.
Then we can finally create the pencil sketch by mixing the grayscale image with the inverted blurry image.
This can be done by dividing the grayscale image by the inverted blurry image. Since images are just arrays,
we can easily do this programmatically using the divide function from the cv2 library in Python.<br> 

I have commented out sections of the code so that you directly get the final result. But you can play around with the code and see 
how it actually works step by step.<br>

<b>Note: </b> Please provide proper path of the location where you have saved your image.
