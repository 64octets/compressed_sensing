"""
Test script. Run Fourier decomposition on a 2D image and see what we get.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import  misc
import BasicFunctions as bf
import Sketching as sketch

# Parameters.
IMAGE_PATH = "../../data/"
IMAGE_NAME = "lenna.png"
SIZE = (75, 75)
K = 1000

# Import the image.
img = misc.imresize(bf.rgb2gray(bf.imread(IMAGE_PATH + IMAGE_NAME)), SIZE)

# Obtain Fourier basis.
basis, coefficients = sketch.basisFourier(img, K)

# Compute reconstruction.
reconstruction = (basis * coefficients).reshape(img.shape)
reconstruction = np.absolute(reconstruction)
    
# Plot.
plt.figure(1); plt.imshow(reconstruction, cmap="gray"); plt.show()