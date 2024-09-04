from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt

def main():
  fig,axs = plt.subplots(2,3)

  # read image and crop it to be square
  A = imread('car.jpg')
  B = np.mean(A, -1); # Convert RGB to grayscale
  rows, cols = B.shape
  centerX = int(rows/2)
  centerY = int(cols/2)
  B = B[centerX-350:centerX+350, centerY-350:centerY+350]

  # show image
  axs[0][0].imshow(B.real, cmap='gray', vmin=0, vmax=255)
  axs[0][0].axis('off')

  rows, cols = B.shape
  centerX = int(rows/2)
  centerY = int(cols/2)
  print(rows, cols)
 
  # fft and show the spectrum
  Bt = np.fft.fft2(B)
  Bt = np.fft.fftshift(Bt)
  mag = np.log(1+np.abs(Bt))
  amin = int(np.amin(mag))
  amax = int(np.amax(mag)) + 1
  a10 = axs[1][0].imshow(mag, cmap='gray', vmin=amin, vmax=amax)
  axs[1][0].axis('off')

  # high pass
  # generate the mask
  r = 80
  mask = np.ones(B.shape)
  mask *= 10
  x, y = np.ogrid[:rows, :cols]
  mask_area = (x - centerX) ** 2 + (y - centerY) ** 2 <= r*r
  mask[mask_area] = 0

  # apply the mask and show the masked spectrum
  Ct = Bt;
  Ct = Ct * mask
  mag = np.log(1+np.abs(Ct))
  axs[1][1].imshow(mag, cmap='gray', vmin=amin, vmax=amax)
  axs[1][1].axis('off')
 
  # ifft and show the image
  Ct = np.fft.ifftshift(Ct)
  A = np.fft.ifft2(Ct)
  axs[0][1].imshow(A.real, cmap='gray', vmin=0, vmax=255)
  axs[0][1].axis('off')
  plt.imshow(A.real, cmap='gray', vmin=0, vmax=255)
  plt.savefig('img2.png', bbox_inches='tight')

  # low pass
  # generate the mask
  r = 20
  mask = np.zeros(B.shape)
  x, y = np.ogrid[:rows, :cols]
  mask_area = (x - centerX) ** 2 + (y - centerY) ** 2 <= r*r
  mask[mask_area] = 1

  # apply the mask and show the masked spectrum
  Ct = Bt;
  Ct = Ct * mask
  mag = np.log(1+np.abs(Ct))
  axs[1][2].imshow(mag, cmap='gray', vmin=amin, vmax=amax)
  axs[1][2].axis('off')
 
  # ifft and show the image
  Ct = np.fft.ifftshift(Ct)
  A = np.fft.ifft2(Ct)
  axs[0][2].imshow(A.real, cmap='gray', vmin=0, vmax=255)
  axs[0][2].axis('off')

  plt.show()

if __name__ == '__main__':
    main()
