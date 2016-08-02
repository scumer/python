# coding=utf-8

import gdcm
from struct import *
import binascii

import struct

filename = r'E:\Project\Python\PyQt\306.dcm'

#reader = gdcm.ImageReader()
#reader.SetFileName(filename)
#reader.Read()
#H:unsigned short
#s:string (array of char)
#L:unsigned long
#HHL
#struct(endian_chr + "HH2sH")

#group, elem, length = element_struct_unpack(bytes_read) implict
#reader.GetImage()

# dcm_file = open(filename,'rb')
# dcm_file.seek(128+4)
# #print dcm_file.read(8)

# bytes_read = dcm_file.read(8)
# group, elem, VR, length = unpack("<HH2sH", bytes_read)

# #print unpack("<HH2sH", bytes_read)



# a=12.34
# b= struct.pack('f', a)

# #print struct.unpack('f', b)

# import binascii


rd = gdcm.ImageReader()
rd.SetFileName(filename)
img = rd.GetImage()
print img.GetPixelFormat()

print img.GetPixelFormat().GetScalarTypeAsString()


