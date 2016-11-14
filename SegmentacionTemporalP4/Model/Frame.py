'''
Created on 4 nov. 2016

@author: jasonsolano
'''
from StdSuites.Type_Names_Suite import null
import numpy as np
import cv2
import cv
import Image
import tensorflow as tf

class Frame():
    frame      = null
    frameHsv   = null
    frameH     = null
    normHist   = null 
    


    def __init__(self, pFrame):
        self.frame = pFrame

    def convertToHSV(self):
        self.frameHsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        
    def splitHSV(self):
        self.frameH,s,v = cv2.split(self.frameHsv)   
    
    def makeNormHist(self):
        self.convertToHSV()
        self.splitHSV()
        cv2.normalize(self.frameH,self.frameH,0,255,cv2.NORM_MINMAX)
        hist = cv2.calcHist([self.frameH],[0],None,[255],[0,255])
        self.normHist = np.divide(hist,hist.sum())
    
    def makeNormHistTensorflow(self):
        self.convertToHSV()
        self.splitHSV()
        size = tf.constant((self.frameHsv.size/3), dtype=tf.float32)
        nbins = tf.constant(255)
        value_range = tf.constant([0.0, 255.0])
        value = tf.convert_to_tensor( self.frameH, dtype=tf.float32 )
        with tf.Session() as sess:
            hist = tf.histogram_fixed_width(value, value_range, nbins)
            normalize = tf.constant( hist.eval(), dtype=tf.float32 )
            self.normHist = tf.div(normalize, size)
            sess.close()
            
        

        