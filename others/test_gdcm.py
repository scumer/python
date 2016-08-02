# -*- coding: utf-8 -*-

import gdcm

cecho = gdcm.CompositeNetworkFunctions()
ret   = cecho.CEcho('192.168.1.109', 1043)
print ret

pre = gdcm.PresentationContext()
print pre