#!/usr/bin/python3
from tkinter import *

class Criar_Label:
    def __init__(self,root2,texto,abcissa,ordenada,fonte,fundo):
        self.label=Label(root2,text=texto,font=fonte,bg=fundo)
        self.label.place(x=abcissa,y=ordenada)
#root = Tk()

#fonte=("Roboto",10)
#titulo=("Roboto",12)
#fundo="Magenta"

#loi=Label(root,text="Olá Mundo",font=fonte, bg=fundo)
#loi.pack()

#canvas=Canvas(root, width=40, height=60, bg=fundo)
#canvas.pack()

#canvas.create_line(0,10,200,10)

#root.mainloop()
