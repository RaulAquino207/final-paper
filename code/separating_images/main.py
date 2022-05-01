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

dict_array = []

idx = 0
lenFile = 0

for r, d, f in os.walk(path):
   for filename in f:
      image = cv2.imread('./samples/{0}'.format(filename))
      grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      rows, cols = grayscale_img.shape
      half_sized_img = cv2.resize(grayscale_img, (int(cols/3), int(rows/3)))
      ret, threshold_img = cv2.threshold(half_sized_img, 80, 255, cv2.THRESH_BINARY)
      horizontally_img = np.concatenate((half_sized_img, threshold_img), axis=1)
      number_of_black_pixels = np.sum(threshold_img == 0)
      idx, lenFile = formatFilename(filename)
      
      dict_array.append({
         'number_of_black_pixels' : number_of_black_pixels,
         'img' : image #FIX THIS
      })

dict_array = sorted(dict_array, key = lambda i: i['number_of_black_pixels'], reverse=True)

number_test = 1
for count, img_infos in enumerate(dict_array):
   aux_name = '00000{0}'.format(number_test)
   if(len(aux_name) > 6):
      aux_name = aux_name.lstrip("0")

   img_infos['aux_name'] = aux_name
   cv2.imwrite(os.path.join('./images_listed', '{0}{1}'.format(aux_name, filename[idx : lenFile])), img_infos['img'])
   number_test += 1
