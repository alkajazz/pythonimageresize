#!/usr/bin/env python2.7

import os
import sys
import getopt
import PIL
from PIL import Image, ImageOps

#for root, directories, filenames in os.walk('/Volumes/Users/nbooth/Desktop/shell/'):
#  8     for directory in directories:
#        9         print os.path.join(root, directory)

def Command():
    
    # Get arg from command line

    opts, args = getopt.getopt(sys.argv[1:], 'd:w:h:')
    directory = ''
    basewidth = -1
    baseheight = -1
    
    # reassign variables based on user input
    
    for opt, arg in opts:
	if opt == '-d':
	    directory = arg
	elif opt == '-w':
	    basewidth = int(arg)
	elif opt == '-h':
	    baseheight = int(arg)

    for image in os.listdir(directory):
    	print('Resizing image' + image)
    	size = (1200, 1200)
    	img = Image.open(os.path.join(directory, image))
    	img2 = ImageOps.fit(img, size, Image.ANTIALIAS)
    	img2.save(os.path.join(directory, 'resized-' + image))
    	print "Batch Processing Complete"


Command()
