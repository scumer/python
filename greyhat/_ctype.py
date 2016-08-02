# coding=utf-8
from ctypes import *
msvcrt = cdll.msvcrt
msg = 'HHHH\n'

msvcrt.printf('T:%s', msg)


print c_int()
