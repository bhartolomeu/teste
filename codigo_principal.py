from tkinter import *
from criar_label import *

def menu():
    root=Tk()
    xy=[]
    xy.append(1)
    xy.append(40)
    fonte=("Roboto",10)
    titulo=("Roboto",12)
    fundo="Magenta"

    a=Criar_Label(root,"Olá Mundo",xy[0],xy[1],fonte,fundo)
    b=Criar_Label(root,"Oi bart",xy[0],xy[1]+30,fonte,fundo)

    root.mainloop()

menu()
