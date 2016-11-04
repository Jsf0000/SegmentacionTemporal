'''
Created on 3 nov. 2016

@author: jasonsolano
'''

import numpy as np
import cv2

class Video:
    '''
    classdocs
    '''

        
    def setVideo(self, direccion):
        cap = cv2.VideoCapture(direccion)
        while(cap.isOpened()):
            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
x = Video()
x.setVideo("/Users/jasonsolano/Documents/Lenguajes/Proyecto4/Videos/Video.mp4")      
        
        