#!/usr/bin/env python2.7

import os
import sys
import getopt
import argparse
from PIL import Image


# command line functions



def Command():
    opts, args = getopt.getopt(sys.argv[1:], 'd:w:h:')
    directory = ''
    width = -1
    height = -1
    
    for opt, arg in opts:
	if opt == '-d':
	    directory = arg
	elif opt == '-w':
	    width = int(arg)
	elif opt == '-h':
	    height = int(arg)
    
    for image in os.listdir(directory):
	print('Resizing image' + image)

	img = Image.open(os.path.join(directory, image))

	img = img.resize((width, height), Image.BILINEAR)

	img.save(os.path.join(directory, 'resized-' + image))

	print "Batch Processing complete"


Command()

 




