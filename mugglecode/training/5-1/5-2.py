#compress image
#click -> dosomething

from PIL import Image as Img
from tkinter import *
from tkinter.filedialog import *

# ui
# ui update
# bussiness

info = {
    'path':[]
}

def make_app():
    app = Tk()
    Label(app, text='Image compress tool',font=('Hack',20,'bold')).pack()
    Listbox(app, name='lbox',bg='#f2f2f2').pack(fill=BOTH,expand=True)
    Button(app, text='open',COMMAND=ui_getdata).pack()
    Button(app, text='compress',COMMAND=compress).pack()
    app.geometry('300x400')
    return app

def ui_getdata():
    f_names = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = f_names
    if info['path']:
        for name in f_names:
            lbox.insert(END, name.split('/')[-1])

def compress():
    for f_path in info['path']:
        output = '/Users/admin/Desktop/output'
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        image.save(output+'c_'+name, quality=60)

app = make_app()
app.mainloop()

