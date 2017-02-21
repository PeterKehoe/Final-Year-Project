# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:40:38 2017

@author: Peter
"""

import ProfileInput 
import DeviceProfile
import glob
import json
from Tkinter import *

def deleteButton():
    selection = LB.curselection()
    for s in selection:
        os.remove("DeviceProfiles"+selection[s]+".json")

def saveButton():
    saveDic = dict.fromkeys(entryLabels)
    for i in saveDic:
        saveDic[i] = fields[i].get()
        fields[i].delete(0,len(saveDic[i]))
    if saveDic["File Name"] in profiles:
        print "this one"
    if True in [saveDic["File Name"] in x for x in profiles]:
        if tkMessageBox.askokcancel("Overwrite", "A Profile with this name already exists, Do you wish to over write it?", icon='warning'):
            ProfileInput.writeProfile(saveDic,"DeviceProfiles")
    #json.dump(saveDic)
        
#    dev.ID = E1.get()
#    E1.delete(0,len(dev.ID))
    
def loadButton():
    selection = lb.curselection()
    
def getPanel(parent, ori):
    pan = PanedWindow(parent, orient = ori)
    pan.pack(fill=BOTH, expand=1)
    return pan
    
def getLabeledBox(Text):
    pan = PanedWindow()
    lab = Label(pan, text = Text)
    lab.pack(side = LEFT)
    box = Entry(pan,bd=5)
    box.pack(side=RIGHT)
    return pan, box
    
panLayer1 = getPanel(None, VERTICAL)
panLayer2 = getPanel(panLayer1, HORIZONTAL)
panLayer3 = getPanel(panLayer1, HORIZONTAL)
panLayer4 = getPanel(panLayer2, VERTICAL)
panLayer5 = getPanel(panLayer2, VERTICAL)

#Layer One
panLayer1.add(panLayer2)
panLayer1.add(panLayer3)

#Layer Two
panLayer2.add(panLayer4)
panLayer2.add(panLayer5)

#Layer Four
entryLabels = ["File Name", "Availible Memory","Make","Model","Port","Place Holder"]
fields= {}
for l in entryLabels:
    pan, box = getLabeledBox(l)
    panLayer4.add(pan)    
    fields[l] = box
    

#Layer Three
Button(panLayer3,text="Save",command = saveButton).pack(fill=BOTH, expand=1, side=RIGHT)
Button(panLayer3,text="Load",command = loadButton).pack(fill=BOTH, expand=1, side=RIGHT)
Button(panLayer3,text="Delete",command = deleteButton).pack(fill=BOTH, expand=1, side=RIGHT)

#Layer Five
lb = Listbox(panLayer5,selectmode=SINGLE)
pathProfiles = glob.glob("DeviceProfiles/*.json")
profiles = []
for p in pathProfiles:
    name = ((p.split("\\")[1]).split("."))[0]
    profiles.append(name)
    lb.insert(i,name)
    i+=1
lb.pack()

mainloop()