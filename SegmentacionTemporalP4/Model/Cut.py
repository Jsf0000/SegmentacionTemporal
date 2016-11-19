'''
Created on 12 nov. 2016

@author: jasonsolano
'''
import timeit
import numpy as np
from Bhattacharyya import Bhattacharyya
from Carbon.Aliases import false

class Cut(object):

    frames        = []
    cuts          = []
    dissimilarity = []

    def __init__(self, pFrames):
        self.frames = pFrames
        
    
    def setArrayDissimilarityTensorFlow(self): 
        start = timeit.default_timer()
        i = 0
        while(i + 1 < (len(self.frames) -1)):
            self.frames[i].makeNormHistTensorflow()
            self.frames[i+1].makeNormHistTensorflow()
            histN1 = self.frames[i].normHist
            histN2 = self.frames[i+1].normHist
            bhattacharyya = Bhattacharyya()
            batta = bhattacharyya.bhattacharyyaDistanceTensorFlow(histN1, histN2)
            print batta
            self.dissimilarity.append(batta)
            i = i + 1
        stop = timeit.default_timer()
        print stop - start
        
    def setArrayDissimilarity(self): 
        i = 0
        while(i + 1 < (len(self.frames) -1)):
            self.frames[i].makeNormHist()
            self.frames[i+1].makeNormHist()
            histN1 = self.frames[i].normHist
            histN2 = self.frames[i+1].normHist
            bhattacharyya = Bhattacharyya()
            batta = bhattacharyya.bhattacharyyaDistance(histN1, histN2)
            self.dissimilarity.append(batta)
            i = i + 1
        stop = timeit.default_timer()

    def calCuts(self):
        devMedia = np.median(self.dissimilarity) + np.std(self.dissimilarity)
        for i in range(len(self.dissimilarity)):
            if (self.dissimilarity[i] >= devMedia):
                if ((i in self.cuts) == False):
                    self.cuts.append(i)
                elif (((i+1) in self.cuts) == False):
                    self.cuts.append(i+1)
        print self.cuts            
                        
            
            
            