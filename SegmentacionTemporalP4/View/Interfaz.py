'''
Created on 15 nov. 2016

@author: jasonsolano
'''
import sys

from StdSuites.Type_Names_Suite import null

class Interfaz():
    video  = null
    opcion = null

    
       
    def ingresarDatos(self):
        self.video = raw_input("Ingrese la direccion del video: ").strip()
        self.opcion = int(raw_input("1: sin  tensorFlow / 2: con tersorFlow").strip())
        
        
        
            