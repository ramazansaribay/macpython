from tkinter import *
from tkinter import ttk
from tkinter import filedialog

window = Tk()

window.title("Ondulasyon Düşme Programı")

window.geometry('350x200')

lbl = Label(window, text="Merhaba")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

def clicked():

    res = "Welcome to " + txt.get()

    lbl.configure(text= res)

def button(self):
    self.button = ttk.Button(self.labelFrame, text = "Seç",command = self.fileDialog)
    self.button.grid(column = 2, row = 0)

def fileDialog(self):

    self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Bir dosya seçin", filetype =
    (("raw dosyası","*.raw"),("tüm dosyalar","*.*")) )
    self.label = ttk.Label(self.labelFrame, text = "")
    self.label.grid(column = 3, row = 0)
    self.label.configure(text = self.filename)

window.mainloop()