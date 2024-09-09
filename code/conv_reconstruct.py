import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve
from scipy import special
from scipy.integrate import quad
import sys

plt.rcParams.update({
    'font.size': 15,               # Set global font size
    'figure.figsize': (6, 2) 
})

# Step 1: Generate a signal
tot_points = 500 # points in the signal we will visualize
rate = 10 # sampling rate is 1/(rate + 1)
num_samples = int(tot_points / (rate + 1))
tot_points = (rate + 1) * num_samples + 1 # include the last sample
#print(tot_points, num_samples)

t = np.linspace(0, 2 * np.pi, tot_points)
# Frequencies of the sine waves
freq1 = 1
freq2 = 2
freq3 = 3
# Amplitudes of the sine waves
amp1 = 1.0
amp2 = 0.5
amp3 = 0.3
# Generating the sine waves
sine1 = amp1 * np.sin(2 * np.pi * freq1 * t)
sine2 = amp2 * np.sin(2 * np.pi * freq2 * t)
sine3 = amp3 * np.sin(2 * np.pi * freq3 * t)
# Adding the sine waves
signal = sine1 + sine2 + sine3

# Generate samples
x_points = np.linspace(0, tot_points - 1, tot_points)
y_points = np.zeros(tot_points)
for i in range(0, tot_points, rate):
    #y_points[i] = i+3
    #y_points[i] = np.random.randint(1, 11)
    y_points[i] = signal[i]

# Filters
def hat_filter_1d(x, width=1):
    return 1 - np.abs(x-width) / width
hat_filter = hat_filter_1d(np.arange(0, 2 * rate + 1, 1), rate)

# Function to generate a 1D Box filter
def box_filter_1d(x, width=1):
    x = x - width
    if (width % 2 == 0):
      return np.where((x > -width / 2) & (x <= width / 2), 1, 0)
    else:
      return np.where((x >= -width / 2) & (x <= width / 2), 1, 0)
box_filter = box_filter_1d(np.arange(0, 2 * rate + 1, 1), rate)
#box_filter = np.ones([rate])

# Function to generate a 1D Gaussian filter
def gaussian_1d(x, mu=0, sigma=1):
    gaussian = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    return gaussian

mu = 0  # Mean
sigma = rate/2  # Standard deviation
delta = 0
rate = rate + delta
x = np.arange(-rate, rate+1, 1)

gaussian_filter_raw = gaussian_1d(x, mu, sigma) - gaussian_1d(rate, mu, sigma)
gaussian_filter = gaussian_filter_raw / (np.max(gaussian_filter_raw)+0.000)

plt.plot(x, gaussian_filter, marker='o')
plt.plot(x, np.pad(hat_filter, (delta, delta), 'constant'), marker='o')
plt.plot(x, np.pad(box_filter, (delta, delta), 'constant'), marker='o')

# Perform the convolution
y_convolved_box = convolve(y_points, box_filter, mode='same', method='auto')
y_convolved_hat = convolve(y_points, hat_filter, mode='same', method='auto')
y_convolved_gaussian = convolve(y_points, gaussian_filter, mode='same', method='auto')

# Plot the original points and the reconstructed continuous signal
plt.figure(figsize=(10, 6))
plt.plot(x_points, y_convolved_box, label='Box Filter', marker='')
plt.plot(x_points, y_convolved_hat, label='Hat Filter', marker='')
plt.plot(x_points, y_convolved_gaussian, label='Gaussian Filter', marker='')
plt.plot(x_points, signal, label='Orignal Signal', marker='')
plt.title('Signal Reconstruction')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

sys.exit()


# Function to generate a 1D sinc function
def sinc_1d(x):
    return np.sinc(x)

# Parameters for the plot
x = np.linspace(-10, 10, 500)  # 500 points between -10 and 10

# Generate the sinc function values
sinc_values = sinc_1d(x)

# Plot the sinc function
plt.plot(x, sinc_values)
plt.title('1D Sinc Function')
plt.xlabel('x')
plt.grid(True)
plt.show()

