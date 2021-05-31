import random
import time
import operator
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.scrolledtext as st
import csv
import json
import sys

class GuiItem:
    def __init__(self, window, label, rowIndex, min=0, max=100 ):
        self.name = label
        self.lbl = Label(window)
        self.lbl.config(text=str(label))
        self.lbl.grid(column=0, row=rowIndex, pady=5)

        self.chk = Checkbutton(window, variable=IntVar())
        self.chk.grid(column=3, row=rowIndex, pady=5)

        self.spinMin = Spinbox(window, from_=min, to=max, width=3)
        self.spinMax = Spinbox(window, from_=min, to=max, width=3)
        self.spinMin.grid(column=4, row=rowIndex, padx=(30,4))
        self.spinMax.grid(column=5,row=rowIndex,pady=5,padx=3)

        self.rndChkVar = IntVar(window, value=0)
        self.rndChk = Checkbutton(window, variable=self.rndChkVar, command=self.randomToggle)
        self.rndChk.grid(column=6, row=rowIndex, pady=5, padx=3)
        
        rnd = round(float(self.getRandomValue()),1)
        var = DoubleVar()
        var.set(rnd)
        print(var)
        self.scale = Scale(window, from_=min, to=max, orient=HORIZONTAL, variable=var)
        self.scale.grid(column=1, row=rowIndex)

        self.entry = Entry(window, width=5, textvariable=var)
        self.entry.grid(column=2, row=rowIndex)
        
        print("GUI item created at index ", rowIndex)


    def updateEntry(self):
        scale = self.scale.get()
        self.entry.delete(0,END)
        self.entry.insert(0,round(float(scale)))


    def updateScale(self):
        entry = self.entry.get()
        self.scale.set(entry)
    def getDataDict(self):
        #Checking if item is to be sent
        value = float(0.0)
        if self.chk.state():
            #Checks if value is to be randomized or manually inputted
            if (self.rndChk.state()) or (self.entry.get() == ''): 
                value = float(self.getRandomValue())
            #Makes sure entry isn't empty
            elif self.entry.get() != '': 
                value = float(self.entry.get())
        else:
            value = None    

        #Returns data and value as a tuple
        return (self.name, value)


    def getRandomValue(self):
        if self.spinMax.get() == '':
            print("Max random value for", self.name, "not selected, using default of 100")
            rndMax = 100
        else:
            rndMax = self.spinMax.get()
        if self.spinMin.get() == '':
            print("Min random value for", self.name, "not selected, using default of 0")
            rndMin = 0
        else:
            rndMin = self.spinMin.get()

        return float(round(random.uniform(float(rndMin), float(rndMax)), 1))

    def syncEntries(self):
        print(self)
        scale = self.scale.get()
        entry = self.entry.get()        
        if self.entry.get() != scale:
            f = float(self)
            self.entry.delete(0,END)
            self.entry.insert(0,round(f,1))
        if self.scale.get() != entry:
            self.scale.set(float(self))

    def randomToggle(self):
        if 'selected' in self.rndChk.state():
            self.entry.config(state='disabled')
            self.scale.config(state='disabled')
        else:
            self.entry.config(state='normal')
            self.scale.config(state='normal')

        

class Gui:
    def __init__(self, queue):
        self.window = Tk()
        self.window.title("DripDash Requester")
        self.window.geometry('700x450')
        self.rows = []

        ##TOP MENU BAR
        self.menuBar = Menu(self.window)
        self.window.config(menu=self.menuBar)
        self.fileMenu = Menu(self.menuBar, tearoff=False)
        self.fileMenu.add_command(label="Load default settings")#, command=self.loadFromFile)
        #fileMenu.add_command(label="Save as new settings", command=##ADD)
        #fileMenu.add_command(label="Open settings from file")
        #fileMenu.add_separator()
        #fileMenu.add_command(label="Exit", command=self.quit)



        self.lbl = Label(self.window, text="DripDashGUI Tester")
        self.lbl.grid(column=0, row=0)
        self.queue = queue
        self.start = False

        ######TOP ROW NAME,START ETC
        self.startBtn = Button(self.window, text="Run", command=self.toggle)
        self.startBtn.grid(column=1, row=0, pady=5, padx=2)
        self.stopBtn = Button(self.window, text="Stop", command=self.toggle)
        self.stopBtn.grid(column=2, row=0, pady=5, padx=2)
        
        self.defaultBtn = Button(self.window, text="Default", command=self.loadFromFile)
        self.defaultBtn.grid(column=4, row=0, pady=5, padx=2)

        self.v = StringVar(self.window, value="http://localhost:8080/collect")
        self.urlEntered = Entry(self.window, width=30, textvariable=self.v)
        self.urlEntered.grid(column=0,row=1, pady=5, padx=2) 

        self.elfs = Combobox(self.window)
        self.elfs['values']= ("WaterElf-1221")
        self.elfs.grid(column = 1, row=1, pady=5)
        self.elfs.current(0)

        ##ADD NEW ROW 
        addRowIdx = (len(self.rows)+3)
        print(addRowIdx)
        v = StringVar(self.window, value='')
        self.addNewLbl = Entry(self.window, width = 30, textvariable=v)
        self.addNewLbl.grid(column=0, row=addRowIdx)
        self.addNewMin = Spinbox(self.window, from_=0, to=999999, width=3)
        self.addNewMin.insert(0,0)
        self.addNewMax = Spinbox(self.window, from_=0, to=999999, width=3)
        self.addNewMax.insert(0,10000)
        self.addNewMin.grid(column=1, row=addRowIdx)
        self.addNewMax.grid(column=2, row=addRowIdx)
        anmn = self.addNewMin.get()
        anmx = self.addNewMax.get()
        anlb = self.addNewLbl.get()
        print(str(anlb))
        self.addNewBtn = Button(self.window, text="Add", command = self.newRow)
        self.addNewBtn.grid(column=3, row=addRowIdx)

        ##LOGBOX
        self.logbox = st.ScrolledText(self.window, width=50,height=10)
        self.logbox.grid(column=0,columnspan=4, row=10, pady=10, padx=3)


        ##LABELS
        lblCurrentVal = Label(self.window, text="Value")
        lblSend = Label(self.window, text="Send")
        lblMin = Label(self.window, text="Min")
        lblMax = Label(self.window, text="Max")
        lblRnd = Label(self.window, text="Random")
        lblCurrentVal.grid(column=2, row=1)
        lblSend.grid(column=3, row=1)
        lblMax.grid(column=4, row=1, padx=(30,4))
        lblMin.grid(column=5, row=1)
        lblRnd.grid(column=6, row=1)
        self.window.after(0, self.scanForDataToSend)
        self.window.mainloop()


    def newRow(self):
        label = self.addNewLbl.get()
        min = self.addNewMin.get()
        max = self.addNewMax.get()
        if min == '':
            min = 0
        if max == '':
            max = 1000
        rowIdx = len(self.rows)
        print(label)
        if label != '':
            item = GuiItem(self.window, label, rowIdx+2, min, max)
            print("New row presseed")
            self.rows.append(item)
            self.updateAddNew(rowIdx+3)
        else: 
            print("missing label")
        
        self.btn = Button(self.window, text="Delete Row", command=lambda: self.rows.remove([x.lbl for x in self.rows].index(label)))
        self.btn.grid(column=7,row=rowIdx+2)

    def newRowFromFunc(self, label, min, max):
        rowIdx = len(self.rows)
        if min == '':
            min = 0
        if max == '':
            max = 1000
        if label == '':
            label = "Default" + str(rowIdx)
        item = GuiItem(self.window, label, rowIdx+2, min, max)
        self.rows.append(item)
        self.updateAddNew(rowIdx+3)

        self.btn = Button(self.window, text="Delete Row", command=lambda: self.rows.pop(rowIdx))
        self.btn.grid(column=7,row=rowIdx+2)

    def removeRow(self, index):
        item = self.rows[index]
        item.destroy()

    def updateAddNew(self, newRowIdx):
        self.addNewLbl.grid(row=newRowIdx)
        self.addNewMin.grid(row=newRowIdx)
        self.addNewMax.grid(row=newRowIdx)
        self.addNewBtn.grid(row=newRowIdx)

    def getAllItems(self):
        items = {}
        for i in self.rows:
            items = items | i.getDataDict
        return items
    
    def toggle(self):
    
        if self.start == False:
            self.start = True
            self.startBtn.config(state='disabled')
            self.urlEntered.config(state='disabled')
            self.stopBtn.config(state='normal')
            self.logbox.delete('1.0',END)
            self.logbox.insert(INSERT, 'Starting requests')
        else:
            self.start = False
            self.urlEntered.config(state='normal')
            self.startBtn.config(state='normal')
            self.stopBtn.config(state='disabled')
            self.logbox.insert(INSERT, 'Stopping requests')
            
    def getUrl(self):
        return str(self.urlEntered.get()) + "/" + str(self.elfs.get())

    def runGui(self):
        self.window.mainloop()

    def setQueue(self, q):
        self.queue = q

    def getQueue(self, q):
        return self.queue

    def loadFromList(self, arr):
        ##@arr = Array made up of 3 items tuple (name, min, max), e.g.: [(x,y,z),(a,b,c),...]
        for i in arr:
            self.newRowFromFunc(i[0],i[1],i[2])

    def loadFromFile(self):
        ##Load list of parameters from csv file stored in assets folder
        try:
            with open('./assets/default_params.csv', newline='') as fp:
                reader = csv.reader(fp)
                for row in reader:
                    if not row[0] in [x.name for x in self.rows]:
                        self.newRowFromFunc(row[0],row[1],row[2])

        except FileNotFoundError as err:
            print(err)

            

    def scanForDataToSend(self):
        print("Are we sending data? ", self.start)
        if self.start == True:
            wholeDict = {}
            for i in self.rows:
                d = i.getDataDict()
                wholeDict.update({d[0] : d[1]})
            url = self.getUrl() 
            job = (wholeDict,url)
            self.queue.put(job)
            self.printRequestToLogbox(job)
        self.window.after(5000, self.scanForDataToSend)


    def printRequestToLogbox(self, job):
        self.logbox.delete('1.0',END)
        self.logbox.insert(INSERT, "URL: " + job[1] + '\n')
        dataDict = job[0]
        #d = json.dumps(dataDict, indent=4)
        print("THIS IS JOB: ", job)
        for i in dataDict:
            print(i)
            self.logbox.insert(INSERT, i + ": " + str(dataDict[i]) + "\n")


    def quit(self):
        self.window.quit()
        sys.exit()

    