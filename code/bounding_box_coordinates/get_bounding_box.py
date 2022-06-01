import os
import cv2
import numpy as np
import time
import shutil
import json

path = './test'

# arr = json.loads("classifications_test.json")
# print(arr)

file = open('./classifications_test.json')
data = json.load(file)
print(len(data))

for r, d, f in os.walk(path):
   for counter, filename in enumerate(f):
      image = cv2.imread('./test/{0}'.format(filename))
      rows, cols = image.shape[:2]
      print(rows, cols)
      for imageInfo in [image for image in data if image['image_name']==filename]:
         filenameTXT = filename.replace('.png', '.txt')
         file = open('./test/{0}'.format(filenameTXT), 'w+')
         for cell in imageInfo['classifications']:
            x = cell['nucleus_x']
            y = cell['nucleus_y']
            x1 = x-100
            x2 = x+100
            y1 = y+100
            y2 = y-100
            if(x1 < 0):
               x1 = 0
            if(y2 < 0):
               y2 = 0
            if(x2 > cols):
               x2 = cols
            if(y1 > rows):
               y1 = rows
            
            cell_class = 0
            if(cell['bethesda_system'] == 'Negative for intraepithelial lesion'):
               cell_class = 0
            if(cell['bethesda_system'] == 'ASC-US'):
               cell_class = 1
            if(cell['bethesda_system'] == 'ASC-H'):
               cell_class = 2
            if(cell['bethesda_system'] == 'LSIL'):
               cell_class = 3
            if(cell['bethesda_system'] == 'HSIL'):
               cell_class = 4
            if(cell['bethesda_system'] == 'SCC'):
               cell_class = 5
            file.write('{0} {1} {2} {3} {4}\n'.format(cell_class, x/cols, y/rows, 416/rows, 416/cols))
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 0), 2)
         file.close()
      cv2.imshow('image original', image)
      cv2.waitKey(0)