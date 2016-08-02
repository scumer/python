from PyQt4.QtGui import *
from PyQt4.QtCore import *
from enum import Enum

class PosState(Enum):
    Outside=0,
    Inside=1,
    P0=2,
    P1=3,
    P2=4,
    P3=5,
    E0=6,
    E1=7,
    E2=8,
    E3=9

def ComputePointStateInRect(point,rect,tolerance):
    state = PosState.Outside
    # point x,y
    px = point.x()
    py = point.y()
    
    #rect point0:LeftTop point3:RightLower
    rx = rect.x()
    ry = rect.y()
    rw = rect.width()
    rh = rect.height()
    rp0 = QPointF(rx,ry)
    rp3 = QPointF(rx+rw,ry+rh)
    
    # Figure out where we are in the widget. Exclude outside case first.
    if (px < (rp0.x()-tolerance) or px > (rp3.x()+tolerance) 
     or py < (rp0.y()-tolerance) or py > (rp3.y()+tolerance)): 
        state = PosState.Outside
    else: # we are on the boundary or inside the border
        e0 = px > rp0.x()-tolerance and px < rp0.x()+tolerance
        e1 = px > rp3.x()-tolerance and px < rp3.x()+tolerance
        e2 = py > rp0.y()-tolerance and py < rp0.y()+tolerance
        e3 = py > rp3.y()-tolerance and py < rp3.y()+tolerance    
        
        # point check
        if e0 and e2:
            state = PosState.P0
        elif e1 and e2:
            state = PosState.P1
        elif e0 and e3:
            state = PosState.P2   
        elif e1 and e3:
            state = PosState.P3
        elif (e0 or e1 or e2 or e3):
            if e0:
                state = PosState.E0
            elif e1:
                state = PosState.E2
            elif e2:
                state = PosState.E1
            elif e3:
                state = PosState.E3
        else:
            state = PosState.Inside
    
    return state

if __name__ == '__main__':
    point = QPointF(20.0,25.0)
    rect = QRectF(10,30,40,80)
    tolerance = 5
    print 'point',point
    print 'rect',rect
    ComputePointStateInRect(point, rect, tolerance)

