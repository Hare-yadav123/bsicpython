'''from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")


def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
    
    
label=Label(root,font=('ds-digital', 80),background='green',foreground='cyan')
label.pack(anchor='center')

time()

mainloop()'''


'''from tkinter import *
from tkinter.ttk import *

from time import strftime

#sine=Tk()

#title("clock")

def time():
    ram=strftime("%H:%M:%S %p")
    label.config(text=ram)
    label.after(2000,time)
    
label=Label(font=('hree',150),background='black',foreground='cyan')
label.pack(anchor='center')
time()

mainloop()'''

from tkinter import*
from tkinter.ttk import*
from time import strftime

son=Tk()
son.title("Haree")

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
    
label=Label(son,font=("Haree",200),foreground="cyan",background="black")
label.pack(anchor='center')

time()
mainloop()
