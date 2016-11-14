'''
Created on 14 nov. 2016

@author: jasonsolano
'''
import csv

class MakeCSV(object):
    cuts = []


    def __init__(self, pCuts):
        self.cuts = pCuts
    
    
    def makeCSV(self):
        out = csv.writer(open("myfile.csv","w"), delimiter=';',quoting=csv.QUOTE_ALL)
        for i in range(len(self.cuts)):
            data = ["Numero de frame: ",self.cuts[i]]
            out.writerow(data)
            
            
