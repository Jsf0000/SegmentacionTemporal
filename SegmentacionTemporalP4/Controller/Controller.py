'''
Created on 12 nov. 2016

@author: jasonsolano
'''

import os
import sys
import site
from StdSuites.Type_Names_Suite import null
from Model.Video import Video
from Model.Bhattacharyya import Bhattacharyya

class Controller():
    video = null 

    def probar(self):
        self.video = Video()
        self.video.setVideo("/Users/jasonsolano/Documents/Lenguajes/Proyecto4/Videos/Video.mp4")
        self.video.frames[1].makeNormHist()
        self.video.frames[2].makeNormHist()
        batt = Bhattacharyya()
        print batt.bhattacharyyaDistance(self.video.frames[1].normHist,self.video.frames[2].normHist)
        
x = Controller()
x.probar()