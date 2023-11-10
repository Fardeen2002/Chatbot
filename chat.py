
import wikipedia as wp
from tkinter import *
from tkinter import ttk

win= Tk()

win.geometry("750x250")

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()