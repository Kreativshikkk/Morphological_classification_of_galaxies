from tkinter import *
import os
import shutil
import sys
from PIL import ImageTk, Image

files=[]
pather = 'C:\\Users\\nmago\\PycharmProjects\\astroschool_project\\Никита1\\' # the folder with all non-sorted files in the same place
for f in os.scandir(pather): 
    if f.is_file() and f.path.split('.')[-1].lower() == 'png':
        files.append(f.path)
# print(files)
i = 0
class App:
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack()
        self.but1 = Button(self.frame, text="Эллипс",
            command=self.bt1).pack(side=LEFT)
        self.but2 = Button(self.frame, text="Неправильная",
            command=self.bt2).pack(side=LEFT)
        self.but3 = Button(self.frame, text="Спираль",
            command=self.bt3).pack(side=LEFT)
        self.but4 = Button(self.frame, text="Ошибка",
            command=self.bt4).pack(side=LEFT)
        self.canvas = Canvas(self.root, height=400, width=400)
        self.image = self.canvas.create_image(0, 0, anchor='nw',image=ImageTk.PhotoImage(Image.open(files[0])))
        self.canvas.pack()
        self.root.mainloop()
    def bt1(self):
        global i
        shutil.move(files[i], 'C:\\Users\\nmago\\PycharmProjects\\astroschool_project\\dataset\\Elliptical Galaxies\\')
        # folder 1 path
        i = i + 1
        if i+1 > len(files):
            sys.exit()
        self.img = ImageTk.PhotoImage(file = str(files[i]))
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.canvas.update()

    def bt2(self):
        global i
        shutil.move(files[i], 'C:\\Users\\nmago\\PycharmProjects\\astroschool_project\\dataset\\Irregular Galaxies\\')
        # folder 2 path
        i = i + 1
        if i+1 > len(files):
            sys.exit()
        self.img = ImageTk.PhotoImage(file = str(files[i]))
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.canvas.update()

    def bt3(self):
        global i
        shutil.move(files[i], 'C:\\Users\\nmago\\PycharmProjects\\astroschool_project\\dataset\\Disk Galaxies\\')
        # folder 3 path
        i = i + 1
        if i+1 > len(files):
            sys.exit() 
        self.img = ImageTk.PhotoImage(file = str(files[i]))
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.canvas.update()
    def bt4(self):
        global i
        shutil.move(files[i], 'C:\\Users\\nmago\\PycharmProjects\\astroschool_project\\dataset\\Error\\')
        # folder 4 path
        i = i + 1
        if i+1 > len(files):
            sys.exit() 
        self.img = ImageTk.PhotoImage(file = str(files[i]))
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.canvas.update()


app= App()