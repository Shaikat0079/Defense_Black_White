import cv2

# read image
img_grey = cv2.imread('desktop.jpg', cv2.IMREAD_GRAYSCALE)

# define a threshold, 128 is the middle of black and white in grey scale
thresh = 128

# threshold the image
img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

# save image
cv2.imwrite('desktop_black_white.jpg', img_binary)
