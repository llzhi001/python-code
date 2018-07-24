from tkinter import *
import os

app = Tk()
label = Label(text='All hidden files',font=('Hack',25,'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2',fg='red')
listbox.pack(fill=BOTH,expand=True)
path = '/Users/Admin'
files = os.listdir(path)
for f in files:
    if f.startswith('.'):
        listbox.insert(END, f)

app.mainloop()
# app.run()

