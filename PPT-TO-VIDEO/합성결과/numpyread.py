import numpy as np
from matplotlib import pyplot as plt

img_array = np.load('2021-11-11_01-38-18.npy')


plt.imshow(img_array)
plt.imsave('filename.jpeg', img_array)
plt.show()
