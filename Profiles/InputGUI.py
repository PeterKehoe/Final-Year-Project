# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:01:51 2017

@author: Peter
"""
import ProfileInput 
import DeviceProfile
import glob
from Tkinter import *   ## notice capitalized T in Tkinter

def deleteButton():
    selection = LB.curselection()
    for s in selection:
        os.remove("DeviceProfiles"+selection[s]+".json")

def addButton():
    dev = DeviceProfile.device()
    dev.ID = E1.get()
    E1.delete(0,len(dev.ID))
    dev.make = E2.get()
    E2.delete(0,len(dev.make))
    dev.model = E3.get()
    E3.delete(0,len(dev.model))
    dev.OFversion = E4.get()
    E4.delete(0,len(dev.OFversion))
    dev.ports = E5.get()
    E5.delete(0,len(dev.ports))
    dev.RuleSize = E6.get()
    E6.delete(0,len(dev.RuleSize))
    
    ProfileInput.writeProfile(dev,"DeviceProfiles")

Lpan = PanedWindow()
Lpan.pack(fill=BOTH, expand=1)
pan = PanedWindow(orient=VERTICAL)


P1 = PanedWindow()
L1 = Label(P1, text = "Device ID")
L1.pack(side = LEFT)
E1 = Entry(P1,bd=5)
E1.pack(side=RIGHT)
pan.add(P1)

P2 = PanedWindow()
L2 = Label(P2, text = "Make")
L2.pack(side = LEFT)
E2 = Entry(P2,bd=5)
E2.pack(side=RIGHT)
pan.add(P2)

P3 = PanedWindow()
L3 = Label(P3, text = "Model")
L3.pack(side = LEFT)
E3 = Entry(P3,bd=5)
E3.pack(side=RIGHT)
pan.add(P3)

P4 = PanedWindow()
L4 = Label(P4, text = "Version")
L4.pack(side = LEFT)
E4 = Entry(P4,bd=5)
E4.pack(side=RIGHT)
pan.add(P4)

P5 = PanedWindow()
L5 = Label(P5, text = "Ports")
L5.pack(side = LEFT)
E5 = Entry(P5,bd=5)
E5.pack(side=RIGHT)
pan.add(P5)

P6 = PanedWindow()
L6 = Label(P6, text = "OF Rule Size")
L6.pack(side = LEFT)
E6 = Entry(P6,bd=5)
E6.pack(side=RIGHT)
pan.add(P6)

P7 = PanedWindow()
addB = Button(P7,text="Save Profile",command = addButton)
addB.pack(side=RIGHT)
pan.add(P7)

Lpan.add(pan)

'''
panR = PanedWindow(orient=VERTICAL)
panR.pack(fill=BOTH, expand=1)
P9 =PanedWindow()
LB = Listbox(P9)
profiles = glob.glob("DeviceProfiles/*.json")
i = 1
LB.insert(1,"Hello")

for p in profiles:
    print p
    LB.insert(i,((p.split("\\")[1]).split("."))[0])
    i+=1

LB.pack()

P8 = PanedWindow()
addB = Button(P8,text="Delete Profile",command = addButton)
addB.pack(side=LEFT)
panR.add(P8)  
'''  

mainloop()