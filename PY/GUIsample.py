from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Ondülasyon Düşüm Programı")
        self.minsize(640, 400)
        self.wm_iconbitmap('icon.ico')

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

        self.button()

window = Tk()

window.title("Ondülasyon Düşüm Programı")

window.geometry('350x200')

lbl = Label(window, text="Dönüşüm yapılacak hamdata dosyasını seçiniz.\nOluştur düğmesine basınız", 
font=("Calibri", 12))

lbl.grid(column=0, row=0)

def button(self):
    self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
    self.button.grid(column = 1, row = 1)

def button(self):
    self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
    self.button.grid(column = 1, row = 1)

window.mainloop()