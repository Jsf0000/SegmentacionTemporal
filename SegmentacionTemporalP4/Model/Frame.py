'''
Created on 4 nov. 2016

@author: jasonsolano
'''
from StdSuites.Type_Names_Suite import null
import numpy as np
import cv2
import Image

class Frame():
    frame      = null
    frameHsv   = null
    frameHNorm = null
    


    def __init__(self, pFrame):
        self.frame = pFrame

    def convertToHSV(self):
        self.frameHsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        #self.frame  = Image.fromarray(self.frame)
        #self.frameHsv = self.frame.convert('HSV')
        #self.frameHsv.show()
       
    


        