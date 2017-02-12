# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 21:01:51 2017

@author: Peter
"""

#Class for switches in the SDN
class device:
    
    def __init__(self,name,ofv,rs):
        self.ID = name
        self.OFversion = ofv
        self.RuleSize = rs
        self.ports = {}
        self.linked = {} 
    
    def addLink(self,portNumber, connectedTo, farPort):
        if portNumber not in self.linked:
            self.linked[portNumber] = None
        if self.linked[portNumber] is not connectedTo:
            self.linked[portNumber] = connectedTo
            connectedTo.addLink(farPort, self, portNumber)
                