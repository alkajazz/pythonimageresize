#!/usr/bin/env python2.7

import os
import sys
import getopt
import argparse
import PIL
from PIL import Image
import numpy as np

# command line functions



def Command():
    opts, args = getopt.getopt(sys.argv[1:], 'd:bw:bh:')
    directory = ''
    basewidth = -1
    baseheight = 1200
    
    for opt, arg in opts:
	if opt == '-d':
	    directory = arg
	elif opt == '-bw':
	    width = int(arg)
	elif opt == '-bh':
	    height = int(arg)
    
    for image in os.listdir(directory):
	print('Resizing image' + image)
        img = Image.open(os.path.join(directory, image))
	#img.load()
	#image_data = np.asarray(img)


	wpercent = (baseheight/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((baseheight,hsize), PIL.Image.ANTIALIAS)

	#new_image = img.fromarray(image_data_new)

        img.save(os.path.join(directory, 'resized-' + image))

	print "Batch Processing complete"


Command()

 




