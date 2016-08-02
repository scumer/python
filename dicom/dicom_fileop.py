# coding=utf-8

import logging
import dicom
from dicom.filereader import read_file
import struct

logger = dicom.logger
#logger.setLevel(logging.DEBUG)

#dicom.debug(True)
#print type(logger.handlers[0])

#H:unsigned short
#s:string (array of char)
#L:unsigned long
#HHL
#struct(endian_chr + "HH2sH")

#group, elem, VR, length = element_struct_unpack(bytes_read) explict
#group, elem, length = element_struct_unpack(bytes_read) implict
filename = r'E:\Project\Python\dicom\306.dcm'

dcm = read_file(filename)
#print dcm[(0x0010, 0x0010)].name
#print dcm[(0x0010, 0x0010)].value
#dcm.decode()
#print dcm.PatientName
#print dcm.get_item(key)
#print dcm.
#print dcm.pixel_array
#print dcm.PixelData
#print dcm.SamplesPerPixel
#print dcm.BitsStored
#print dcm.BitsAllocated
#print dcm.HighBit
#print dcm.SliceLocation
#print dcm.SliceThickness
#print dcm.PixelRepresentation


#fp = open(filename,'rb')
#pre = fp.read(128)
#dcm.clear()

data = dcm.pixel_array

window = dcm.WindowWidth[0]
level = dcm.WindowCenter[0]

import numpy
import numpy as np

a = (data <= (level - 0.5 - (window - 1) / 2),
 data > (level - 0.5 + (window - 1) / 2))

condlist = numpy.array(a, dtype=bool)
print 'len(condlist)',len(condlist)
print 'condlist.ndim',condlist.ndim

totlist = np.logical_or.reduce(condlist, axis=0)#keepdims=False
#condlist = condlist.T
print len(totlist)

print 'totlist.ndim',totlist.ndim
#print [~totlist]
print 'VSTACK:'
#print np.vstack([condlist, ~totlist])
#print np.concatenate([condlist,~totlist],axis=0)
print '-----'
#print np.concatenate([condlist],)

window = 250
level = 40
pmin =  (level - 0.5 - (window - 1.0) / 2.0)
pmax =  (level - 0.5 + (window - 1.0) / 2.0)
data = 100

g1 = lambda data: ((data - (level - 0.5)) / (window - 1) + 0.5) * (255 - 0)
g2 = lambda data: (data-pmin)/float(pmax-pmin)*255.0
pmin =  (level - 0.5 - (window - 1.0) / 2.0)
pmax =  (level - 0.5 + (window - 1.0) / 2.0)
print window,level
print pmin,pmax

print 'g1:',g1(data)
print 'g2:',g2(data)


#print reduce(np.logical_or,condlist)
#print [0, 255, lambda data: ((data - (level - 0.5)) / (window - 1) + 0.5) * (255 - 0)]
#(data,
#[data <= (level - 0.5 - (window - 1) / 2),
 #data > (level - 0.5 + (window - 1) / 2)],
#[0, 255, lambda data: ((data - (level - 0.5)) / (window - 1) + 0.5) * (255 - 0)])


#print dcm.SliceLocation
#print dcm.SliceThickness
#dcm = read_file(r'E:\Project\Python\dicom\307.dcm')
#print dcm.SliceLocation
#print dcm.SliceThickness
#print dcm.PatientName




