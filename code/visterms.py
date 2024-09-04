import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
  # Create a grid of (u, v) values
  u = np.linspace(-5, 5, 100)
  v = np.linspace(-5, 5, 100)
  u, v = np.meshgrid(u, v)
  
  # Compute the function values
  z0 = np.cos(2*u-2*v)
  z1 = np.cos(1*u)
  z2 = np.cos(-2*u+v)
  
  # Create a figure and a set of subplots
  fig = plt.figure(figsize=(10, 10))
  
  ax1 = fig.add_subplot(2, 3, 1, projection='3d')
  ax1.plot_surface(u, v, z0, cmap='Greys', edgecolor='none')
  ax1.set_title('cos(2u - 2v)')
  ax1.set_xlabel('u')
  ax1.set_ylabel('v')
  
  ax2 = fig.add_subplot(2, 3, 2, projection='3d')
  ax2.plot_surface(u, v, z1, cmap='Greys', edgecolor='none')
  ax2.set_title('cos(1u - 0v)')
  ax2.set_xlabel('u')
  ax2.set_ylabel('v')
  
  ax3 = fig.add_subplot(2, 3, 3, projection='3d')
  ax3.plot_surface(u, v, z0, cmap='Greys', edgecolor='none')
  ax3.set_title('cos(-2u + v)')
  ax3.set_xlabel('u')
  ax3.set_ylabel('v')
  
  ax4 = fig.add_subplot(2, 3, 4)
  ax4.imshow(z0, cmap='gray')
  ax4.set_title('cos(2u - 2v)')
  ax4.set_xlabel('u')
  ax4.set_ylabel('v')
  
  ax5 = fig.add_subplot(2, 3, 5)
  ax5.imshow(z1, cmap='gray')
  ax5.set_title('cos(1u - 0v)')
  ax5.set_xlabel('u')
  ax5.set_ylabel('v')
  
  ax6 = fig.add_subplot(2, 3, 6)
  ax6.imshow(z2, cmap='gray')
  ax6.set_title('cos(-2u + v)')
  ax6.set_xlabel('u')
  ax6.set_ylabel('v')
  
  plt.tight_layout()
  plt.show()

if __name__ == '__main__':
    main()
