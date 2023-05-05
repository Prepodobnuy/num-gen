from tkinter import *
from tkinter.ttk import *
from time import sleep
import os


def changeCcode(input:str):
    print(input)
    if input[0] == '+':
        input = input[1::]
    file = open('ccode.cfg', 'w+')
    file.write(input)
    file.close()

def changeCode(input:str):
    file = open('code.cfg', 'w+')
    file.write(input)
    file.close()

def start():
    ccode = open('ccode.cfg')
    code = open('code.cfg')
    filename = ccode.read() + code.read()
    ccode.close()
    code.close()

    file = open('path.cfg', 'w+')
    file.write(f'numberBases/{filename}.txt')
    file.close()

    wrfile = open(f'numberBases/{filename}.txt', 'w+')
    wrfile.close()

    sleep(1)

    os.system('./start')

root = Tk()

root.title("blow job global ofensive")
root.iconphoto(False, PhotoImage(file = "logo.png"))

Label(text='Enter country code [+380/+7/+1]').grid(row=1, column=1, columnspan=3)
Label(text='Enter local operator code [29/44]').grid(row=3, column=1, columnspan=3)

ccEntry = Entry(width=8)
cEntry = Entry(width=8)

Button(width=10, text='change ccode', command= lambda: changeCcode(ccEntry.get())).grid(row=2, column=3)
Button(width=10, text='change code', command= lambda: changeCode(cEntry.get())).grid(row=4, column=3)
Button(width=10, text='start', command= start).grid(row=5, column=1, columnspan=4)

ccEntry.grid(row=2, column=1, columnspan=2)
cEntry.grid(row=4, column=1, columnspan=2)

root.mainloop()