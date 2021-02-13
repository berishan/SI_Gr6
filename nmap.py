from tkinter import *
from tkinter import filedialog
from tkinter import Radiobutton
import nmap3
import tkinter.messagebox
import json 
import re


def validate_url(url):
    return re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", url) or re.match(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", url)
    

def writeToFileResults(res):
        filename = ""
        if variable.get() == "json": 
            filename = "/results.json"
            res = json.dumps(res)
        else:
            filename = "/results.txt"
            res = str(res)
        with open(dirPath+filename, 'a+') as myfile:
            nmap = nmap3.Nmap()
            myfile.write(res+ "\n")
            tkinter.messagebox.showinfo('Successful scan!','The scan results have successfully been saved to '+ dirPath +filename)
        return dirPath+filename

def cmd_flag():
        cmdFlags = ""
        if(var1.get() == 1):
            cmdFlags += "--top-ports 100"
        if(var2.get() == 1):
            cmdFlags += "-sL "
        if(var3.get() == 1):
            cmdFlags += "-O "
        if(var4.get() == 1):
            cmdFlags += "-A "
        if(var5.get() == 1):
            cmdFlags += "-sV "
        return cmdFlags

def scan_nmap():
 
    cmdFlags = cmd_flag()
    nmap = nmap3.NmapScanTechniques()
    if (var8.get() == 2):
        result = nmap.nmap_idle_scan(domain.get(),args=cmdFlags)
        writeToFileResults(result)

    elif (var8.get() == 3):
        result = nmap.nmap_ping_scan(domain.get(),args=cmdFlags)
        writeToFileResults(result)

    elif (var8.get() == 4):
        result = nmap.nmap_syn_scan(domain.get(),args=cmdFlags)
        writeToFileResults(result)

    elif (var8.get() == 5):
      
        result = nmap.nmap_tcp_scan(domain.get(),args=cmdFlags)
        writeToFileResults(result)

    elif (var8.get() == 6):
    
        result = nmap.nmap_tcp_scan(domain.get(), args=cmdFlags)
        writeToFileResults(result)

programTitle = "Automated Nmap Scanner"
widthAndHeight = "400x350"

ws = Tk()
ws.resizable(False, False)
ws.title(programTitle)
ws.geometry(widthAndHeight)                                      #ndryshon size

dirPath = ""


def browse_button():
    filename = filedialog.askdirectory()
    global dirPath
    dirPath = filename
    if dirPath != "":
        browseBtn.configure(text="Chosen path")
    

def scan():                                                  #funksioni qe thirret kur klikohet butoni 
    #  if (validators.url(domain.get()) or validators.ipv4(domain.get())) and dirPath != "":  
    if validate_url(domain.get()) and dirPath !="":
        scan_nmap()
        domain.delete(0, 'end') 
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var8.set(5)
        browseBtn.configure(text="Browse folder")
    else:
         tkinter.messagebox.showinfo('ERROR!','Please fill the fields properly!')

Label(ws, text="Enter Domain:").place(x=90, y=20)
domain =Entry(ws)
domain.place(x=175, y=20)

comm = LabelFrame(ws, text="Commands Available")
comm.place(x=30, y=50)           #frame 1
 
techn = LabelFrame(ws, text="Scanning Techniques")
techn.place(x=250, y=50)        #frame 2
                     

var1 = IntVar()
Checkbutton(comm, text="Top Port Scan", variable=var1, onvalue=1).pack()
var2 = IntVar()
Checkbutton(comm, text="List Scan", variable=var2, onvalue=1).pack()
var3 = IntVar()
Checkbutton(comm, text=" OS Detection", variable=var3, onvalue=1).pack()
var4 = IntVar()
Checkbutton(comm, text="Service Detection", variable=var4, onvalue=1).pack()
var5 = IntVar()
Checkbutton(comm, text="Version Detection", variable=var5, onvalue=1).pack()


var8 = IntVar()
Radiobutton(techn, text="Idle Scan", variable=var8, value=2).pack()
Radiobutton(techn, text="Ping Scan", variable=var8, value=3).pack()
Radiobutton(techn, text="SYN Scan", variable=var8, value=4).pack()
Radiobutton(techn, text="TCP Scan", variable=var8, value=5).pack()
Radiobutton(techn, text="UDP Scan", variable=var8, value=6).pack()
var8.set(value=5)


Label(ws, text="Save the results at:").place(x=50, y=220)
browseBtn = Button(text="Browse folder", command=browse_button)
browseBtn.place(x=169, y=220)

variable = StringVar(ws)
variable.set("json") # default value

w = OptionMenu(ws, variable, "json", "plain text")

w.place(x=260,y=216)

submitBtn = Button(ws, text="Scan", command=scan, width=15, height=2)           #butoni   
submitBtn.place(x=145, y=265)  

ws.mainloop()



