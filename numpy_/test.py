import numpy as np

import random
from flask import jsonify

def fun():
    try:
        raise '3'
    except Exception as e:
        #return '2',4
        print jsonify({'error': 1}), 500

#print fun()
print jsonify(['1','2'])

import json

#a = np.arange10).reshape(2,5)
#print a
#print a*2+1

