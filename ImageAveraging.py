import cv2
import numpy as np
from matplotlib import pyplot as plt


img1 = cv2.imread('gbr.jpg',0)
img2 = cv2.imread('gbr1.jpg',0)
img3 = cv2.imread('gbr.jpg',0)


avg_img = cv2.addWeighted(img1, 1/3, img2, 1/3, 0)
avg_img = cv2.addWeighted(avg_img, 1, img3, 1/3, 0)


plt.subplot(121),plt.imshow(img1,cmap = 'gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(avg_img,cmap = 'gray')
plt.title('Hasil Image Averaging'), plt.xticks([]), plt.yticks([])
plt.show()
