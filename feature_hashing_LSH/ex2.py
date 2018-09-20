from PIL import Image
import numpy as np
from resizeimage import resizeimage

def grey_and_rescale(filename):
    with open(filename, 'r+b') as f:
        with Image.open(f) as image:
            image = image.convert('L')                                          #Greyscale the image
            image = resizeimage.resize_cover(image, [9, 8])                     #Resize the image
            image.load()
            image_data = np.asarray( image, dtype="int32" )                     #Load the image as a numpy array
            return image_data

def compareValues(tab):
    ret=[]
    for row in tab:
        curs = []
        for i in range(len(row)-1):
            if row[i] > row[i+1]:
                curs.append(True)
            else:
                curs.append(False)
        ret.append(curs)
    return ret

def hashFunc(tab):
    ret = []
    for difference in tab:
    	decimal_value = 0
    	hex_string = []
    	for index, value in enumerate(difference):
    		if value:
    			decimal_value += 2**(index % 8)
    		if (index % 8) == 7:
    			hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
    			decimal_value = 0
    	ret.append(hex_string)
    return ''.join(str(e) for e in ret)

print("--- Greyscaled and resized images ---")
pic1 = grey_and_rescale("pic1.png")
pic2 = grey_and_rescale("pic2.png")
pic3 = grey_and_rescale("pic3.png")

print(pic1)
print(pic2)
print(pic3)

print("--- Differences ---")
res1 = np.asarray(compareValues(pic1))
res2 = np.asarray(compareValues(pic2))
res3 = np.asarray(compareValues(pic3))

print(res1)
print(res2)
print(res3)

print("--- hash ---")
hash1 = hashFunc(res1)
hash2 = hashFunc(res2)
hash3 = hashFunc(res3)

print(hash1)
print(hash2)
print(hash3)
