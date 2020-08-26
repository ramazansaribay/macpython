from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Ondülasyon Düşüm Programı")
        self.minsize(640, 400)
        
        self.labelFrame = ttk.LabelFrame(self, text = "Hamdata Dosyası Seç")
        self.labelFrame.grid(column = 1, row = 0, padx = 20, pady = 20)

        self.button()
    
    ond = Entry(window,width=10)
    ond.grid(column=4, row=0)

    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Seç",command = self.fileDialog)
        self.button.grid(column = 2, row = 0)

    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Bir dosya seçin", filetype =
        (("raw dosyası","*.raw"),("tüm dosyalar","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 3, row = 0)
        self.label.configure(text = self.filename)
        
        f = open(self.filename, "r")
        gs = f.readlines()
        x = (gs [9::18])
        for line in x:
            line = line.replace("GS,","")
            line = line.replace("PN","")
            line = line.replace("N ","")
            line = line.replace("E ","")
            line = line.replace("EL","")
            line = line.split(",")
        text_file = open("sample.txt", "w")
        n = text_file.write('Welcome to pythonexamples.org')
        text_file.close()
        
root = Root()
root.mainloop()