# -*- coding: utf-8 -*-

"""
复制VS工程，提供源路径、目的路径名称，复制源路径下所有文件至目的路径下(排除x64和win32目录)，
并且将后缀为.vcxproj、.vcxproj.filters、.vcxproj.user的文件名改为目的路径名称
"""
"""
复制
"""

import os
import shutil

# src_path = raw_input('src path:')
src_path = r'E:\Project\VS_project\vtkKSW\test'
# dst_path = raw_input('dst path:')
dst_path = r'E:\Project\VS_project\vtkKSW\VR_MPR'

# print os.listdir(src_path)
# shutil.copy(src_path,dst_path)   
# print os.system(r'copy E:\Project\VS_project\vtkKSW\test\main.cpp E:\Project\VS_project\vtkKSW\VR_MPR\m.cpp')
# for file in os.listdir(src_path):
# 	# print file
# 	if file == 'x64' or file == 'Win32':
# 		continue
# 	# copyfun = lambda src,dst :
# 	filename = os.path.join(src_path, file)
# 	if os.path.isfile(filename):
# 		file_path = os.path.split(filename) #分割出目录与文件
# 		if file == file_path[1]+'.vcxproj' or file == file_path[1]+'.vcxproj':
# 			os.system('copy /Y %s %s'%)
# 	# else
#




