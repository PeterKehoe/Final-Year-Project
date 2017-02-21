#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 21:01:51 2017

@author: Peter
"""
import json
#Class for switches in the SDN
class device():
    
    def __init__(self):
        self.ID = ""
        self.make = ""
        self.model= ""
        self.OFversion = ""
        self.RuleSize = ""
        self.ports = {}
        self.linked = {} 
    
    def addLink(self,portNumber, connectedTo, farPort):
        if portNumber not in self.linked:
            self.linked[portNumber] = None
        if self.linked[portNumber] is not connectedTo:
            self.linked[portNumber] = connectedTo
            connectedTo.addLink(farPort, self, portNumber)
    
    def writeJson(self):
        return json.dumps({"ID":self.ID,
                           "make":self.make,
                           "model":self.model,
                           "Version":self.OFversion,
                           "RuleSize":self.RuleSize,
                           "Ports":self.ports,
                           "Links":self.linked})