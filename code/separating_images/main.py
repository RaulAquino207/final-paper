import os
import cv2
import numpy as np

path = './samples'
#Navigating the path where the images are.

def formatFilename(filename):
   idx = 0
   for i in range(0, len(filename)):
      if(filename[i] == '.'):
         idx = i

   return idx, len(filename)

idx = 0
lenFile = 0
for r, d, f in os.walk(path):
   for filename in f:
      img = cv2.imread('./samples/{0}'.format(filename))
      grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      rows, cols = grayscale_img.shape
      half_sized_img = cv2.resize(grayscale_img, (int(cols/3), int(rows/3)))
      ret, threshold_img = cv2.threshold(half_sized_img, 80, 255, cv2.THRESH_BINARY)
      horizontally_img = np.concatenate((half_sized_img, threshold_img), axis=1)
      number_of_black_pix = np.sum(threshold_img == 0)
      idx, lenFile = formatFilename(filename)
      if(number_of_black_pix <= 1500):
         cv2.imwrite(os.path.join('./images_listed', '{0}{1}'.format(number_of_black_pix, filename[idx : lenFile])), img)
      else:
         cv2.imwrite(os.path.join('./images_listed', '{0}{1}'.format(number_of_black_pix, filename[idx : lenFile])), img)
      cv2.imshow('image', horizontally_img)
      cv2.waitKey(0)