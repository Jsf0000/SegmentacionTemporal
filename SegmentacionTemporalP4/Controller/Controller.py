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
from View.Interfaz import Interfaz
class Controller():
    video = null
    Csv   = null
    interfaz = null 

    def sinTensorflow(self,pVideo):
        self.video = Video()
        self.video.setVideo(pVideo)
        c = Cut(self.video.frames)
        c.setArrayDissimilarity()
        c.calCuts()
        self.Csv = MakeCSV(c.cuts)
        self.Csv.makeCSV()
    def conTersorflow(self,pVideo):
        self.video = Video()
        self.video.setVideo(pVideo)
        c = Cut(self.video.frames)
        c.setArrayDissimilarityTensorFlow()()
        c.calCuts()
        self.Csv = MakeCSV(c.cuts)
        self.Csv.makeCSV()
        
    def controlar(self):
        self.interfaz =  Interfaz()
        self.interfaz.ingresarDatos()
        if (self.interfaz.opcion == 1):
            self.sinTensorflow(self.interfaz.video)
        elif (self.interfaz.opcion == 2):
            self.conTersorflow(self.interfaz.video)
        else:
            print "Error"
        
           
    
        
x = Controller()
x.sinTensorflow("/Users/jasonsolano/Documents/Lenguajes/Proyecto4/Videos/Video.mp4")
