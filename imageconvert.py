#!/usr/bin/env python2.7

import os
import sys
import getopt
import PIL
from PIL import Image

def Command():
    opts, args = getopt.getopt(sys.argv[1:], 'd:w:h:')
    directory = ''
    basewidth = -1
    baseheight = -1
    
    for opt, arg in opts:
	if opt == '-d':
	    directory = arg
	elif opt == '-w':
	    basewidth = int(arg)
	elif opt == '-h':
	    baseheight = int(arg)

    for image in os.listdir(directory):

	if basewidth > -1:
	    print('Resizing image' + image)
	    img = Image.open(os.path.join(directory, image))
	    wpercent = (basewidth/float(img.size[0]))
	    hsize = int((float(img.size[1])*float(wpercent)))
	    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
	    img.save(os.path.join(directory, 'resized-' + image))
	    print "Batch Processing Complete"
	
	else:
	    print('Resizing Image' + image)
	    img = Image.open(os.path.join(directory, image))
	    wpercent = (baseheight/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
	    img = img.resize((baseheight,hsize), PIL.Image.ANTIALIAS)
            img.save(os.path.join(directory, 'resized-' + image))
	    print "Batch Processing complete"


Command()

 




