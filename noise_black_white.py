from statistics import median
from numpy import average

from wand.image import Image

with Image(filename="desktop_black_white.jpg") as img:
    img.noise("poisson", attenuate=0.9)
    img.save(filename="noiseBW.jpg")


with Image(filename="desktop_black_white.jpg") as img:
    img.noise("laplacian", attenuate=1.0)
    img.save(filename="noiseBW2.jpg")


import cv2

img = cv2.imread('noiseBW.jpg')

# Apply bilateral filter with d = 15,
sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img, 15, 75, 75)
# Save the output.
cv2.imwrite('desktop_bilateral_BW.jpg', bilateral)
# Apply Average filter
average = cv2.blur(img, (5, 5))
# Save the output.
cv2.imwrite('desktop_average_BW.jpg', average)
# Apply Gaussian Filter
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imwrite('desktop_gaussian_BW.jpg', gaussian)
median_filter = cv2.medianBlur(img, 5)
cv2.imwrite('desktop_median_BW.jpg', median_filter)


img2 = cv2.imread('noiseBW2.jpg')

# Apply bilateral filter with d = 15,
sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img2, 15, 75, 75)
# Save the output.
cv2.imwrite('desktop_bilateral_BW2.jpg', bilateral)
# Apply Average filter
average = cv2.blur(img2, (5, 5))
# Save the output.
cv2.imwrite('desktop_average_BW2.jpg', average)
# Apply Gaussian Filter
gaussian = cv2.GaussianBlur(img2, (5, 5), 0)
cv2.imwrite('desktop_gaussian_BW2.jpg', gaussian)
median_filter = cv2.medianBlur(img2, 5)
cv2.imwrite('desktop_median_BW2.jpg', median_filter)
