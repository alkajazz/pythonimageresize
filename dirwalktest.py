#!/usr/bin/env python2.7

# /Volumes/Users/nbooth/Desktop/shell\ script/

import os

#f = []
#for root, directories, filenames in os.walk('/Volumes/Users/nbooth/Desktop/shell/'):
#    for directory in directories:
#    	filepath = os.path.join(root, directory)
#    	f.append(filepath)
#
#    	print filepath


rootpath = '/Volumes/Users/nbooth/Desktop/shell/'
dirlist = []
for root, dirs, files in os.walk('/Volumes/Users/nbooth/Desktop/shell/'):
    dirlist += dirs

#f = []
#for x in dirlist:
#	f.append("{}{}".format(rootpath, x))

print dirlist
