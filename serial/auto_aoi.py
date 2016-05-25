# coding=utf-8

import serial
import binascii

d_check = '010300000001840a'
d_reply = '01030200017984'

#modify 1

port = serial.Serial('COM1')

while True:
    if port.inWaiting() > 6:
        data = port.read_all()
        hdata = binascii.b2a_hex(data)
        print hdata

        if hdata == d_check:
            port.write(binascii.a2b_hex(d_reply))
        else:
            port.write(data)


port.close()

