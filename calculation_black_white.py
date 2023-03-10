import cv2
from skimage import metrics


ref_img = cv2.imread("desktop_black_white.jpg")
img1 = cv2.imread("noiseBW.jpg")
img2 = cv2.imread("desktop_average_BW.jpg")
img3 = cv2.imread("desktop_bilateral_BW.jpg")
img4 = cv2.imread("desktop_gaussian_BW.jpg")
img5 = cv2.imread("desktop_median_BW.jpg")


# Mean square error

mse_skimg1 = metrics.mean_squared_error(ref_img, img1)
print("MSE: based on scikit-image = ", mse_skimg1)
mse_skimg2 = metrics.mean_squared_error(ref_img, img2)
print("MSE: based on scikit-image Average_Filtering = ", mse_skimg2)
mse_skimg3 = metrics.mean_squared_error(ref_img, img3)
print("MSE: based on scikit-image Bilateral_Filtering = ", mse_skimg3)
mse_skimg4 = metrics.mean_squared_error(ref_img, img4)
print("MSE: based on scikit-image Gaussian_Filtering = ", mse_skimg4)
mse_skimg5 = metrics.mean_squared_error(ref_img, img5)
print("MSE: based on scikit-image Median_Filtering = ", mse_skimg5)
# mse_skimg6 = metrics.mean_squared_error(ref_img, ref_img)
# print("MSE: based on scikit-image No_Filtering = ", mse_skimg6)



print('=======================================================')
print('=======================================================')

# Peak Signal Noise Ratio

psnr_skimg1 = metrics.peak_signal_noise_ratio(ref_img, img1)
print("PSNR: based on scikit-image = ", psnr_skimg1)
psnr_skimg2 = metrics.peak_signal_noise_ratio(ref_img, img2)
print("PSNR: based on scikit-image Average_Filtering= ", psnr_skimg2)
psnr_skimg3 = metrics.peak_signal_noise_ratio(ref_img, img3)
print("PSNR: based on scikit-image Bilateral_Filtering= ", psnr_skimg3)
psnr_skimg4 = metrics.peak_signal_noise_ratio(ref_img, img4)
print("PSNR: based on scikit-image Gaussian_Filtering= ", psnr_skimg4)
psnr_skimg5 = metrics.peak_signal_noise_ratio(ref_img, img5)
print("PSNR: based on scikit-image Median_Filtering= ", psnr_skimg5)



print('=======================================================')
print('=======================================================')

# Normalized Root Mean Square Error

nrmse_skimg1 = metrics.normalized_root_mse(ref_img, img1)
print("NRMSE: based on scikit-image = ", nrmse_skimg1)
nrmse_skimg2 = metrics.normalized_root_mse(ref_img, img2)
print("NRMSE: based on scikit-image Average_Filtering= ", nrmse_skimg2)
nrmse_skimg3 = metrics.normalized_root_mse(ref_img, img3)
print("NRMSE: based on scikit-image Bilateral_Filtering= ", nrmse_skimg3)
nrmse_skimg4 = metrics.normalized_root_mse(ref_img, img4)
print("NRMSE: based on scikit-image Gaussian_Filtering= ", nrmse_skimg4)
nrmse_skimg5 = metrics.normalized_root_mse(ref_img, img5)
print("NRMSE: based on scikit-image Median_Filtering= ", nrmse_skimg5)



print("=======================================================")
print("=======================================================")
print("2nd Iteration")

print("=======================================================")
print("=======================================================")
img6 = cv2.imread("noiseBW2.jpg")
img7 = cv2.imread("desktop_average_BW2.jpg")
img8 = cv2.imread("desktop_bilateral_BW2.jpg")
img9 = cv2.imread("desktop_gaussian_BW2.jpg")
img10 = cv2.imread("desktop_median_BW2.jpg")


# Mean square error

mse_skimg6 = metrics.mean_squared_error(ref_img, img6)
print("MSE: based on scikit-image = ", mse_skimg6)
mse_skimg7 = metrics.mean_squared_error(ref_img, img7)
print("MSE: based on scikit-image Average_Filtering = ", mse_skimg7)
mse_skimg8 = metrics.mean_squared_error(ref_img, img8)
print("MSE: based on scikit-image Bilateral_Filtering = ", mse_skimg8)
mse_skimg9 = metrics.mean_squared_error(ref_img, img9)
print("MSE: based on scikit-image Gaussian_Filtering = ", mse_skimg9)
mse_skimg10 = metrics.mean_squared_error(ref_img, img10)
print("MSE: based on scikit-image Median_Filtering = ", mse_skimg10)
# mse_skimg6 = metrics.mean_squared_error(ref_img, ref_img)
# print("MSE: based on scikit-image No_Filtering = ", mse_skimg6)



print('=======================================================')
print('=======================================================')

# Peak Signal Noise Ratio

psnr_skimg6 = metrics.peak_signal_noise_ratio(ref_img, img6)
print("PSNR: based on scikit-image = ", psnr_skimg6)
psnr_skimg7 = metrics.peak_signal_noise_ratio(ref_img, img7)
print("PSNR: based on scikit-image Average_Filtering= ", psnr_skimg7)
psnr_skimg8 = metrics.peak_signal_noise_ratio(ref_img, img8)
print("PSNR: based on scikit-image Bilateral_Filtering= ", psnr_skimg8)
psnr_skimg9 = metrics.peak_signal_noise_ratio(ref_img, img9)
print("PSNR: based on scikit-image Gaussian_Filtering= ", psnr_skimg9)
psnr_skimg10 = metrics.peak_signal_noise_ratio(ref_img, img10)
print("PSNR: based on scikit-image Median_Filtering= ", psnr_skimg10)



print('=======================================================')
print('=======================================================')

# Normalized Root Mean Square Error

nrmse_skimg6 = metrics.normalized_root_mse(ref_img, img6)
print("NRMSE: based on scikit-image = ", nrmse_skimg6)
nrmse_skimg7 = metrics.normalized_root_mse(ref_img, img7)
print("NRMSE: based on scikit-image Average_Filtering= ", nrmse_skimg7)
nrmse_skimg8 = metrics.normalized_root_mse(ref_img, img8)
print("NRMSE: based on scikit-image Bilateral_Filtering= ", nrmse_skimg8)
nrmse_skimg9 = metrics.normalized_root_mse(ref_img, img9)
print("NRMSE: based on scikit-image Gaussian_Filtering= ", nrmse_skimg9)
nrmse_skimg10 = metrics.normalized_root_mse(ref_img, img10)
print("NRMSE: based on scikit-image Median_Filtering= ", nrmse_skimg10)
