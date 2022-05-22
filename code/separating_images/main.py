import os
import cv2
import numpy as np
import time

path = './samples'

def formatFilename(filename):
   idx = 0
   for i in range(0, len(filename)):
      if(filename[i] == '.'):
         idx = i

   return idx, len(filename)

dict_array = []

idx = 0
lenFile = 0
start_time = time.time()

for r, d, f in os.walk(path):
   for filename in f:
      image = cv2.imread('./samples/{0}'.format(filename))
      grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      rows, cols = grayscale_img.shape
      half_sized_img = cv2.resize(grayscale_img, (int(cols/3), int(rows/3)))
      ret, threshold_img = cv2.threshold(half_sized_img, 80, 255, cv2.THRESH_BINARY)
      number_of_black_pixels = np.sum(threshold_img == 0)
      idx, lenFile = formatFilename(filename)
      
      dict_array.append({
         'number_of_black_pixels': number_of_black_pixels,
         'filename': filename
      })

dict_array = sorted(dict_array, key = lambda i: i['number_of_black_pixels'], reverse=True)

value = 1

for count, img_infos in enumerate(dict_array):
   aux_name = '0{0}'.format(value)   
   os.rename('samples/{0}'.format(img_infos['filename']), 'samples/{0}.png'.format(aux_name))
   value += 1

print("--- %s seconds ---" % (time.time() - start_time))
