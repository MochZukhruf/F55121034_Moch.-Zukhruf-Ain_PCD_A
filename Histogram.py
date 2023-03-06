import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('lena.jpg',0)


hist,bins = np.histogram(img.flatten(),256,[0,256])


plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.show()
