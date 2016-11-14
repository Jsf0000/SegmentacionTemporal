'''
Created on 12 nov. 2016

@author: jasonsolano
'''

import os
import sys
import site
from StdSuites.Type_Names_Suite import null
from Model.Video import Video
from Model.Cut import Cut
from MakeCSV import MakeCSV
class Controller():
    video = null
    Csv   = null 

    def probar(self):
        self.video = Video()
        self.video.setVideo("/Users/jasonsolano/Documents/Lenguajes/Proyecto4/Videos/Video.mp4")
        c = Cut(self.video.frames)
        c.setArrayDissimilarity()
        c.calCuts()
        self.Csv = MakeCSV(c.cuts)
        self.Csv.makeCSV()
        
x = Controller()
x.probar()