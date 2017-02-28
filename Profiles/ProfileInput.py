#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:29:55 2017

@author: Peter
"""
import json
import DeviceProfile as dp

def readProfile(fileName):
    try:
        pro = open(fileName,"r")
        att = json.load(pro)
        dev = dp.device()
        #need to initial attributes
        print att
        return dev
    except IOError:
        print "Could not open file",fileName,": Path or file name incorrect"
        return
    
def writeProfile(dev,Path):
    try:
        pro = open(Path+"/"+dev["File Name"]+".json","w+")
        pro.write(json.dumps(dev))
    except IOError:
        print "Could not open file",dev["File Name"],": Path or file name incorrect"

    
