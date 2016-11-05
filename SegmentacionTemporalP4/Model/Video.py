'''
Created on 3 nov. 2016

@author: jasonsolano
'''

import numpy as np
import cv2
from Frame import Frame
class Video:
    frames = []
    
    def setVideo(self, direccion):
        cap = cv2.VideoCapture(direccion)
        ret = True
        while(ret):
            ret,frame = cap.read()
            f = Frame(frame)
            self.frames.append(f)
        cap.release()
        
        
        
x = Video()
x.setVideo("/Users/jasonsolano/Documents/Lenguajes/Proyecto4/Videos/Video.mp4")
print len(x.frames)
x.frames[1].convertToHSV()
cv2.imshow('frame',x.frames[1].frameHsv)
cv2.waitKey(0)
      
        