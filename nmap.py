from tkinter import *
from tkinter import filedialog
from tkinter import Radiobutton
import validators
import nmap3
from tkinter import *
import tkinter.messagebox
import json 

def writeToFileResults(res):
        with open(dirPath+'/results.txt', 'a+') as myfile:
            nmap = nmap3.Nmap()
            myfile.write(str(res) + "\n")

            tkinter.messagebox.showinfo('Successful scan!','The scan results have successfully been saved to '+ dirPath +"/results.txt")

def scan_nmap():
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

    if (var8.get() == 2):
        results = tcp_scan(domain.get(),cmdFlags)
        writeToFileResults(results)

    elif (var8.get() == 3):    
        os_results = nmap.nmap_os_detection(domain.get()) 
        writeToFileResults(os_results)

    elif (var8.get() == 4):
        results = tcp_scan(domain.get(),cmdFlags)
        writeToFileResults(results)

    elif (var8.get() == 5):
        results = tcp_scan(domain.get(),cmdFlags)
        writeToFileResults(results)
    
    elif (var8.get() == 6):
        results = tcp_scan(domain.get(),cmdFlags)
        writeToFileResults(results)
    

ws = Tk()
ws.resizable(False, False)
ws.title("NMAP SCAN")
ws.geometry("400x350")                                      #ndryshon size

dirPath = ""


def browse_button():
    filename = filedialog.askdirectory()
    global dirPath
    dirPath = filename
    if dirPath != "":
        browseBtn.configure(text="Path already chosen")
    

def scan():                                                  #funksioni qe thirret kur klikohet butoni 
    if (validators.url(domain.get()) or validators.ipv4(domain.get())) and dirPath != "":
        scan_nmap()
    else:
        tkinter.messagebox.showinfo('ERROR!','Please fill the fields properly!')



def tcp_scan(target,flags=""):
    nmap = nmap3.NmapScanTechniques()
    return nmap.nmap_tcp_scan(target=target,args=flags)

    

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
Radiobutton(techn, text="Fin Scan", variable=var8, value=1).pack()
Radiobutton(techn, text="Idle Scan", variable=var8, value=2).pack()
Radiobutton(techn, text="Ping Scan", variable=var8, value=3).pack()
Radiobutton(techn, text="SYN Scan", variable=var8, value=4).pack()
Radiobutton(techn, text="TCP Scan", variable=var8, value=5).pack()
Radiobutton(techn, text="UDP Scan", variable=var8, value=6).pack()




Label(ws, text="Save the results at:").place(x=110, y=250)
browseBtn = Button(text="Browse folder", command=browse_button)
browseBtn.place(x=230, y=250)

submitBtn = Button(ws, text="Scan", command=scan, width=15, height=2)           #butoni   
submitBtn.place(x=145, y=280)  


labelFile = Label(ws)
labelFile.place(x=30, y=280)
path= Entry(ws)



ws.mainloop()



