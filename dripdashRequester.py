import requests as req
import random
import time
import operator
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.scrolledtext as st


class Data:
    def __init__(self):
        self.waterTemp = None
        self.airTemp = None
        self.humidity = None
        self.light = None
        self.ph = None
        self.rssi = None
        self.beds = []

    def setRandomWaterTemp(self, x,y):
        if x == '':
            x = 0
        if y == '':
            y = 50
        self.waterTemp = float(round(random.uniform(float(x), float(y)), 1))

    def setRandomAirTemp(self, x,y):
        if x == '':
            x = 0
        if y == '':
            y = 50
        self.airTemp = float(round(random.uniform(float(x), float(y)), 1))
    
    def setRandomHumidity(self, x,y):
        if x == '':
            x = 0
        if y == '':
            y = 100
        self.humidity = float(round(random.uniform(float(x), float(y)), 1))
        
    def setRandomLight(self, x,y):
        if x == '':
            x = 0
        if y == '':
            y = 16000
        self.light = float(round(random.uniform(float(x), float(y)), 1))
    
    def setRandomPH(self, x,y):
        if x == '':
            x = 0
        if y == '':
            y = 14
        self.ph = float(round(random.uniform(float(x), float(y)), 1))

    def setWaterTemp(self, x):
        self.waterTemp = float(x)

    def setAirTemp(self, x):
        self.airTemp = float(x)

    def setHum(self, x):
        self.humidity = float(x)

    def setLux(self, x):
        self.light = float(x)

    def setPH(self, x):
        self.ph = float(x)
    
    def generateJsonData(self):
        return {
            'waterTemp': self.waterTemp,
            'airTemp': self.airTemp,
            'humidity': self.humidity,
            'light': self.light,
            'ph': self.ph,
            'rssi': self.rssi
        }
    
    def __str__(self):
        return ("Data send on last Request: \n"+
                "waterTemp: "+str(self.waterTemp)+'\n'+
                "airTemp: "+str(self.airTemp)+'\n'+
                "humidity: "+str(self.humidity)+'\n'+
                "luminosity: "+str(self.light)+'\n'+
                "ph: "+str(self.ph)+'\n')
    
#############################################################################################

headers = {'Content-type': 'application/json'}
url = ''
count = 0
    
def makeRequest():
    global start
    if start == True:
        d = createData()
        print(str(d))
        logbox.delete('1.0',END)
        logbox.insert('insert', str(d))
        try:
            res = req.post(url, json=d.generateJsonData(), headers=headers, timeout=3)
        except:
            print("Request timeout")
        #logbox.insert(INSERT, "Server response: " + str(res.status_code) + '\n')

        #print(res.status_code)    
    window.after(5000, makeRequest)


def createData():
    d = Data()
    if chkWaterTemp.state():
        if 'selected' in chkWaterrnd.state():
            d.setRandomWaterTemp(spinWaterMin.get(),spinWaterMax.get())
        elif not entryWaterTemp.get():
            messagebox.showinfo(title="Missing Field", message="Enter a value for Water Temperature or uncheck the option")
        else:
            wt = entryWaterTemp.get()
            d.setWaterTemp(wt)
        
    if chkAirTemp.state():
            if 'selected' in chkAirrnd.state():
                d.setRandomAirTemp(spinAirMin.get(),spinAirMax.get())
            elif not entryAirTemp.get():
                messagebox.showinfo(title="Missing Field", message="Enter a value for Air Temperature or uncheck the option")
            else:
                at = entryAirTemp.get()
                d.setAirTemp(at)
        
    if chkHumidity.state():
            if 'selected' in chkHumrnd.state():
                d.setRandomHumidity(spinHumMin.get(),spinHumMax.get())
            elif not entryHumidity.get():
                messagebox.showinfo(title="Missing Field", message="Enter a value for Humidity or uncheck the option")
            else:
                hum = entryHumidity.get()
                d.setHum(hum)
        
    if chkLux.state():
            if 'selected' in chkLuxrnd.state():
                d.setRandomLight(spinLuxMin.get(),spinLuxMax.get())
            elif not entryLux.get():
                messagebox.showinfo(title="Missing Field", message="Enter a value for Luminosity or uncheck the option")
            else:
                lux = entryLux.get()
                d.setLux(lux)
        
    if chkPH.state():
            if 'selected' in chkPHrnd.state():
                d.setRandomPH(spinPHMin.get(),spinPHMax.get())
            elif not entryPH.get():
                messagebox.showinfo(title="Missing Field", message="Enter a value for pH or uncheck the option")
            else:
                ph = entryPH.get()
                d.setPH(ph)

    return d
    




############################################################################################3


start = False
def run():
    global start, url
    start = True
    url = urlEntered.get()
    elf = elfs.get()
    url = url + '/' + elf
    startBtn.config(state='disabled')
    urlEntered.config(state='disabled')
    stopBtn.config(state='normal')
    logbox.insert(INSERT, url + '\n')

    

def stop():
    global start
    start = False
    logbox.insert(INSERT, 'stopping' + '\n')
    urlEntered.config(state='normal')
    startBtn.config(state='normal')
    stopBtn.config(state='disabled')
    logbox.insert(INSERT, 'stopped' + '\n')


def updatePH(self):
    f = float(self)
    entryPH.delete(0,END)
    entryPH.insert(0,round(f,1))

def updateAir(self):
    f = float(self)
    entryAirTemp.delete(0,END)
    entryAirTemp.insert(0,round(f,1))

def updateWater(self):
    f = float(self)
    entryWaterTemp.delete(0,END)
    entryWaterTemp.insert(0,round(f,1))

def updateLux(self):
    f = float(self)
    entryLux.delete(0,END)
    entryLux.insert(0,round(f,1))

def updateHum(self):
    f = float(self)
    entryHumidity.delete(0,END)
    entryHumidity.insert(0,round(f,1))

def rndAir():
    if 'selected' in chkAirrnd.state():
        scaleAirTemp.config(state='disabled')
        entryAirTemp.config(state='disabled')
    else:
        scaleAirTemp.config(state='normal')
        entryAirTemp.config(state='normal')

def rndWater():
    if 'selected' in chkWaterrnd.state():
        scaleWaterTemp.config(state='disabled')
        entryWaterTemp.config(state='disabled')
    else:
        scaleWaterTemp.config(state='normal')
        entryWaterTemp.config(state='normal')

def rndHum():
    if 'selected' in chkHumrnd.state():
        scaleHumidity.config(state='disabled')
        entryHumidity.config(state='disabled')
    else:
        scaleHumidity.config(state='normal')
        entryHumidity.config(state='normal')

def rndLux():
    if 'selected' in chkLuxrnd.state():
        scaleLux.config(state='disabled')
        entryLux.config(state='disabled')
    else:
        scaleLux.config(state='normal')
        entryLux.config(state='normal')

def rndPh():
    if 'selected' in chkPHrnd.state():
        scalePH.config(state='disabled')
        entryPH.config(state='disabled')
    else:
        scalePH.config(state='normal')
        entryPH.config(state='normal')




window = Tk()
window.title("DripDash Requester")
window.geometry('640x450')

lbl = Label(window, text="DripDashGUI Tester")
lbl.grid(column=0, row=0)

startBtn = Button(window, text="Run", command=run)
startBtn.grid(column=1, row=0, pady=5, padx=2)
stopBtn = Button(window, text="Stop", command=stop)
stopBtn.grid(column=2, row=0, pady=5, padx=2)

v = StringVar(window, value="http://localhost:8080/collect")
urlEntered = Entry(window, width=30, textvariable=v)
urlEntered.grid(column=0,row=1, pady=5, padx=2)

elfs = Combobox(window)
elfs['values']= ("WaterElf-1221")
elfs.grid(column = 1, row=1, pady=5)
elfs.current(0)

lblCurrentVal = Label(window, text="Value")
lblCurrentVal.grid(column=2, row=1)

lblSend = Label(window, text="Send")
lblMin = Label(window, text="Min")
lblMax = Label(window, text="Max")
lblRnd = Label(window, text="Random")
lblSend.grid(column=3, row=1)
lblMax.grid(column=4, row=1, padx=(30,4))
lblMin.grid(column=5, row=1)
lblRnd.grid(column=6, row=1)


lblAirTemp = Label(window, text="Air Temperature")
lblAirTemp.grid(column=0, row=2, pady=5)
entryAirTemp = Entry(window, width=5)
entryAirTemp.grid(column=2, row=2, pady=5)
scaleAirTemp = Scale(window, from_=0, to=40, orient=HORIZONTAL, command=updateAir)
scaleAirTemp.grid(column = 1, row=2, pady=5)
chkAirTemp = Checkbutton(window, variable=IntVar(), onvalue=1, offvalue=0)
chkAirTemp.grid(column=3, row=2, pady=5)
spinAirMin = Spinbox(window, from_=0, to=45, width=3)
spinAirMax = Spinbox(window, from_=0, to=45, width=3)
spinAirMin.grid(column=4,row=2,pady=5,padx=(30,4))
spinAirMax.grid(column=5,row=2,pady=5,padx=3)
chkAirrndVar = IntVar(window, value=0)
chkAirrnd = Checkbutton(window, variable=chkAirrndVar, command=rndAir)
chkAirrnd.grid(column=6,row=2,pady=5,padx=3)

lblWaterTemp = Label(window, text="Water Temperature")
lblWaterTemp.grid(column=0, row=3, pady=5)
entryWaterTemp = Entry(window, width=5)
entryWaterTemp.grid(column=2, row=3, pady=5)
scaleWaterTemp = Scale(window, from_=0, to=40, orient=HORIZONTAL, command=updateWater)
scaleWaterTemp.grid(column = 1, row=3, pady=5)
chkWaterTemp = Checkbutton(window, variable=IntVar(), onvalue=1, offvalue=0)
chkWaterTemp.grid(column=3, row=3, pady=5)
spinWaterMin = Spinbox(window, from_=0, to=45, width=3)
spinWaterMax = Spinbox(window, from_=0, to=45, width=3)
spinWaterMin.grid(column=4,row=3,pady=5,padx=(30,4))
spinWaterMax.grid(column=5,row=3,pady=5,padx=3)
chkWaterrndVar = IntVar(window, value=0)
chkWaterrnd = Checkbutton(window, variable=chkWaterrndVar, command=rndWater)
chkWaterrnd.grid(column=6,row=3,pady=5,padx=3)

lblHumidity = Label(window, text="Humidity")
lblHumidity.grid(column=0, row=4, pady=5)
entryHumidity = Entry(window, width=5)
entryHumidity.grid(column=2, row=4, pady=5)
scaleHumidity = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=updateHum)
scaleHumidity.grid(column = 1, row=4, pady=5)
chkHumidity = Checkbutton(window, variable=IntVar(), onvalue=1, offvalue=0)
chkHumidity.grid(column=3, row=4, pady=5)
spinHumMin = Spinbox(window, from_=0, to=100, width=3)
spinHumMax = Spinbox(window, from_=0, to=100, width=3)
spinHumMin.grid(column=4,row=4,pady=5,padx=(30,4))
spinHumMax.grid(column=5,row=4,pady=5,padx=3)
chkHumrndVar = IntVar(window, value=0)
chkHumrnd = Checkbutton(window, variable=chkHumrndVar, command=rndHum)
chkHumrnd.grid(column=6,row=4,pady=5,padx=3)

lblLux = Label(window, text="Luminosity")
lblLux.grid(column=0, row=5, pady=5)
entryLux = Entry(window, width=5)
entryLux.grid(column=2, row=5, pady=5)
scaleLux = Scale(window, from_=0, to=16000, orient=HORIZONTAL, command=updateLux)
scaleLux.grid(column = 1, row=5, pady=5)
chkLux = Checkbutton(window, variable=IntVar(), onvalue=1, offvalue=0)
chkLux.grid(column=3, row=5, pady=5)
spinLuxMin = Spinbox(window, from_=0, to=16000, width=3)
spinLuxMax = Spinbox(window, from_=0, to=16000, width=3)
spinLuxMin.grid(column=4,row=5,pady=5,padx=(30,4))
spinLuxMax.grid(column=5,row=5,pady=5,padx=3)
chkLuxrndVar = IntVar(window, value=0)
chkLuxrnd = Checkbutton(window, variable=chkLuxrndVar, command=rndLux)
chkLuxrnd.grid(column=6,row=5,pady=5,padx=3)

lblPH = Label(window, text="pH")
lblPH.grid(column=0, row=6, pady=5)
entryPH = Entry(window, width=5)
entryPH.grid(column=2, row=6, pady=5)
scalePH = Scale(window, from_=0, to=14, orient=HORIZONTAL, command=updatePH)
scalePH.grid(column = 1, row=6, pady=5)
chkPH = Checkbutton(window, variable=IntVar(), onvalue=1, offvalue=0)
chkPH.grid(column=3, row=6, pady=5)
spinPHMin = Spinbox(window, from_=0, to=14, width=3)
spinPHMax = Spinbox(window, from_=0, to=14, width=3)
spinPHMin.grid(column=4,row=6,pady=5,padx=(30,4))
spinPHMax.grid(column=5,row=6,pady=5,padx=3)
chkPHrndVar = IntVar(window, value=0)
chkPHrnd = Checkbutton(window, variable=chkPHrndVar, command=rndPh)
chkPHrnd.grid(column=6,row=6,pady=5,padx=3)


logbox = st.ScrolledText(window, width=50,height=10)
logbox.grid(column=0, columnspan=4, row=7, pady=10, padx=3)

window.after(5000, makeRequest)
window.mainloop()


#############################################################################





