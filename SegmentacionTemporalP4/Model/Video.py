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
        
        
        
#x = Video()
#x.setVideo("/Users/jasonsolano/Documents/Lenguajes/Proyecto4/Videos/Video.mp4")
#x.frames[1].convertToHSV()
#x.frames[1].splitHSV()
#x.frames[1].makeNormHist()
        