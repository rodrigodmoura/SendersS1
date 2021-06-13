# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 20:08:52 2021

@author: Admin
"""
class BackLog:
    
    def __init__(self):
        self.configuration = {"config":None, "sheet": None, "dir":None, "Subject": None, "Msg": None}
        
        
    def getConfiguration(self):
        return self.configuration
    
    def setConfiguration(self, configuration):
        self.configuration = configuration