import cv2
import numpy as np
from matplotlib import pyplot as plt


img1 = cv2.imread('gbr.jpg',0)
img2 = cv2.imread('gbr1.jpg',0)


diff = cv2.absdiff(img1,img2)


plt.subplot(131),plt.imshow(img1,cmap = 'gray')
plt.title('Citra Lena'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img2,cmap = 'gray')
plt.title('Citra gambar'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(diff,cmap = 'gray')
plt.title('Hasil Pengurangan Citra'), plt.xticks([]), plt.yticks([])
plt.show()
