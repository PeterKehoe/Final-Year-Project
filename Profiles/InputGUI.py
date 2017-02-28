import glob, os, json, tkMessageBox,ProfileInput
from Tkinter import *

#Some Gobels
profiles = []
entryLabels = ["File Name", "Availible Memory","Make","Model","Port","Place Holder"]
fields = {}

''' Returns the Path to the directory containing the profiles, as a string 
'''
def getPath(name):
    return "DeviceProfiles/"+name+".json"

''' Clears and repopulates the listbox of profiles
'''
def refreshList():
    del profiles[:]
    lb.delete(0,END)
    pathProfiles = glob.glob(getPath("*"))
    for p in pathProfiles:
        name = ((p.split("\\")[1]).split("."))[0]
        profiles.append(name)
        lb.insert(END,name)

''' Handler for the Delete button
'''
def deleteButton():
    selection = lb.curselection()
    if len(selection)<1:
        tkMessageBox.showinfo("Error","No Profile Seleceted to Delete")
    else:
        for s in selection:
            try:
                os.remove(getPath(lb.get(s)))
            except IOError:
                tkMessageBox.showinfo("Error","Unable to Delete the Selected file")
    refreshList()

''' Handler for Save Button
'''
def saveButton():
    saveDic = dict.fromkeys(entryLabels)
    save = True
    for i in saveDic:
        saveDic[i] = fields[i].get()
        fields[i].delete(0,len(saveDic[i]))
    if saveDic["File Name"] is "":
        save = False
        tkMessageBox.showinfo("Error","No File name was provided!")
    elif saveDic["File Name"] in profiles:
        save = tkMessageBox.askokcancel("Overwrite", "A Profile with this name already exists, Do you wish to over write it?", icon='warning')
    if save:
        ProfileInput.writeProfile(saveDic,"DeviceProfiles")
    refreshList()
    
''' Handler for load button
'''    
def loadButton():
    selection = lb.curselection()
    try:
        if len(selection)<1:
            tkMessageBox.showinfo("Error","No Profile Seleceted to Load")
        else:
            pro = open(getPath(lb.get(selection[0])),"r")
            att = json.load(pro)
            for en in entryLabels:
                fields[en].delete(0,END)
                fields[en].insert(0, att[en])
    except IOError:
        tkMessageBox.showinfo("Error","Unable to open selected profile")

''' Returns a panel with the provided orientation and with the supplied parent container
'''   
def getPanel(parent, ori):
    pan = PanedWindow(parent, orient = ori)
    pan.pack(fill=BOTH, expand=1)
    return pan
 
''' Returns a panel containing a formated label and an entry box
    also returns a reference to the entry box
'''   
def getLabeledBox(Text):
    pan = PanedWindow()
    lab = Label(pan, text = Text)
    lab.pack(side = LEFT)
    box = Entry(pan,bd=5)
    box.pack(side=RIGHT)
    return pan, box
 
#Container Panels   
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

#Layer Four. Left side
for l in entryLabels:
    pan, box = getLabeledBox(l)
    panLayer4.add(pan)    
    fields[l] = box
    
#Layer Three. Bottom
Button(panLayer3,text="Save",command = saveButton).pack(fill=BOTH, expand=1, side=RIGHT)
Button(panLayer3,text="Load",command = loadButton).pack(fill=BOTH, expand=1, side=RIGHT)
Button(panLayer3,text="Delete",command = deleteButton).pack(fill=BOTH, expand=1, side=RIGHT)

#Layer Five. Right side
lb = Listbox(panLayer5,selectmode=SINGLE)
refreshList()
lb.pack()

#Start GUI
mainloop()