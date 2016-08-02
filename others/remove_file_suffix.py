# -*- coding: utf-8 -*-


import re
import os


# 待处理目录名称
pathname = r"D:\Media"
exclude_path = r""
exclude_file = r""

dircnt = 0
for path, subdirs, files in os.walk(pathname, topdown=False):
	dircnt = dircnt + 1
	print dircnt,path
	if(path == exclude_path): #
		continue
	for file in files:
		filename = os.path.join(path,file)
		if(filename == __file__): #
			continue
		if(os.path.isfile(filename)):
			split = os.path.splitext(filename)
			if(split[0] and split[1] and split[1] != '.jpg'):
				os.rename(filename, split[0])

		
		# print filename
		

