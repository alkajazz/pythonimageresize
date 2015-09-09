#!/usr/bin/env python2.7

import os
import sys
import getopt
import PIL
from PIL import Image, ImageOps
import time
import re
from datetime import datetime

opts, args = getopt.getopt(sys.argv[1:], 'd:w:h:')
directory = ''
basewidth = -1
baseheight = -1
   
for opt, arg in opts:
	if opt == '-d':
	    directory = arg
	elif opt == '-w':
	    width = int(arg)
	elif opt == '-h':
	    height = int(arg)
    
f = []
dirlist = []
for root, dirs, files in os.walk(directory):
	dirlist += dirs

        
for x in dirlist:
	f.append("{}{}/".format(directory, x))

def Command():
    for x in f:
    	print x
    	y = os.listdir(x)
        for image in y:
            if image.endswith('.db'):
            	pass
            elif image.endswith('.ini'):
                pass
            else:
                findme = re.compile(r'(?<=\/)[^\/]*(?=\/[^\/]*$)')
                print(' Resizing Image' + image)
                size = (1200, 1200)
                img = Image.open(os.path.join(x, image))
                img2 = ImageOps.fit(img, size)
                filename = re.findall(findme, x)
                img2.save(os.path.join(x, str(filename) + '-' + str(datetime.now().strftime('%m-%d-%Y-%H-%M-%S')) + '.JPG'))
        #        print "batch processing complete"
Command()
