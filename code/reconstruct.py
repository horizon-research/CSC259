import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image and convert it to grayscale
image_path = 'car.jpg'  # Replace with your image path
image = Image.open(image_path).convert('L')  # Convert to grayscale
image_array = np.array(image)

# Perform 2D FFT
fft_result = np.fft.fft2(image_array)

# Shift zero frequency component to the center
fft_result_shifted = np.fft.fftshift(fft_result)

# Create a zeroed array for the modified FFT result
fft_result_modified = np.zeros_like(fft_result_shifted, dtype=complex)

# Get the center position (first term in frequency domain)
rows, cols = fft_result_shifted.shape
center_row, center_col = rows // 2, cols // 2

# Keep only certain frequency components
num = 50
mask = np.zeros_like(fft_result_shifted, dtype=complex)
mask[center_row-num:center_row+num+1, center_col-num:center_col+num+1] = 1 
fft_result_modified = fft_result_shifted * mask

# Inverse FFT to get the image with only the first term
fft_result_inverse_shifted = np.fft.ifftshift(fft_result_modified)
modified_image_array = np.fft.ifft2(fft_result_inverse_shifted).real

# Display the original and modified images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_array, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Reconstruction with Terms \n within cos[-'+str(num)+','+str(num)+'] and cos['+str(num)+',-'+str(num)+']')
plt.imshow(modified_image_array, cmap='gray')
plt.axis('off')

plt.show()

