import json
import os
import time
import math
import av
from PIL import Image
import numpy as np
from rand_index import rand_index
import pims
from multiprocessing import Pool, TimeoutError
from operator import itemgetter


clusters = [set() for _ in range(970)]


def grey_and_rescale(frame):
    image = frame.resize((9,8)).convert('L')
    image_data = np.asarray( image, dtype="int32" )
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
    return ''.join(str(y) for x in ret for y in x)


def processing(filename):
    tab = np.zeros((8, 9))
    frames = []
    container = av.open(filename)
    for i, frame in enumerate(container.decode(video=0)):
        # if i%5 == 0:
        frames.append(grey_and_rescale(frame.to_image()))

    counter = 0
    for i in range(int(len(frames)*0.10), int(len(frames)*0.90)):
        tab = np.add(tab, frames[i])
        counter +=1

    tab = np.divide(tab, counter)
    im_comp = compareValues(tab)
    im_token = hashFunc(im_comp)
    im_hash = int(im_token, 16)

    return filename[:-4], im_hash



pool = Pool(processes=10)

tab_name = []
for root, dirs, filenames in os.walk("videos/"):
    for filename in filenames:

        tab_name.append(os.path.join(root, filename))

d = {}
for f, im_hash in pool.imap_unordered(processing, tab_name, ):
    d[f[7:]] = im_hash;


order = sorted(d.items(), key=itemgetter(1), reverse=True)
for i, t in enumerate(order):
    clusters[i//10].add(t[0])

# print(clusters)

print(rand_index(clusters))
