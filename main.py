import os
from tkinter import *
from tkinter import ttk
from mss.linux import MSS as mss
ls = os.listdir()
if 'monitor-1.png' in ls:
    os.remove('monitor-1.png')
root = Tk()
root.title('Simple shot')
root.geometry('300x150')
root.resizable(width=False, height=False)
def showimage():
    mss().shot()
    panel = Label(root, text = 'Screenshot saved to home directory')
    panel.pack()
btn=ttk.Button(root, text='Screenshot',command=showimage)
btn.pack()
root.mainloop()
