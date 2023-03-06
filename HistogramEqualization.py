import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('lena.jpg',0)


equ = cv2.equalizeHist(img)


plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Gambar Ori'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(equ,cmap = 'gray')
plt.title('Hasil Histogram Equalization'), plt.xticks([]), plt.yticks([])
plt.show()
