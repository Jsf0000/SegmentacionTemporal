'''
Created on 12 nov. 2016

@author: jasonsolano
'''

from StdSuites.Type_Names_Suite import null
import math
import numpy as np
import cv2
import cv
import Image
import tensorflow as tf

class Bhattacharyya(object):
    
    beta  = null
    alpha = null
    
    def MakeBeta(self,histN1,histN2):
         h1sqt = tf.sqrt(histN1)
         h2sqt = tf.sqrt(histN2)
         mhits = tf.mul(h1sqt,h2sqt)
         with tf.Session() as sess:
             sess.run(h1sqt)
             sess.run(h2sqt)
             sess.run(mhits)
             self.beta = np.sum(mhits.eval())
             sess.close()
    
    def makeAlpha(self,histN1,histN2):
        mhist1 = tf.reduce_mean(histN1)
        mhist2 = tf.reduce_mean(histN2)
        with tf.Session() as sess:
            m1 = sess.run(mhist1)
            m2 = sess.run(mhist2)
            self.alpha = 1/(math.sqrt(m1*m2*math.pow(255,2)))
            sess.close()
    
    def bhattacharyyaDistance(self, histN1,histN2):
        self.makeAlpha(histN1, histN2)
        self.MakeBeta(histN1, histN2)
        result = math.sqrt(1 - (self.alpha*self.beta))
        return result
        
             
         
             
    
    
    
   


     
        

        