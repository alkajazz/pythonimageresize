#!/usr/bin/env python2.7

import os
import sys
import getopt
import PIL
from PIL import Image, ImageOps

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
    
print directory

def GetDirList():

    dirlist = []
    for root, dirs, files in os.walk('/Volumes/Users/nbooth/Desktop/shell/'):
    	dirlist += dirs
        for x in dirlist:
        	dirlist.append("{}{}".format(directory, x))
        	print dirlist

#def Command():
                    #    for image in x:
            	    #        print('Resizing image' + image)
            	    #        size = (1200, 1200)
            	    #        img = Image.open(os.path.join(directory, image))
            	    #        img2 = ImageOps.fit(img, size, Image.AntiAlias)
            	    #        img2.save(os.path.join(direcotry, 'resized' + image))
            	    #        print "Batch Processing Complete"


GetDirList()
