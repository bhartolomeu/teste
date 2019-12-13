#!/usr/bin/python3
from tkinter import *

class Criar_Label:
    def __init__(self,root,texto,abcissa,ordenada,fonte,fundo):
         self.label=Label(root)
         self.label["text"]=texto
         self.label["font"]=fonte
         self.label["bg"]=fundo
         self.label.place(x=abcissa,y=ordenada)

#Será que deveríamos fazer polimorfismo aqui e fazer da classe Criar_Label a classe mãe?
class Criar_Label_Titulo:
    def __init__(self,root2,texto,fonte,fundo):
         self.titulo=Label(root2)
         self.titulo["text"]=texto
         self.titulo["font"]=fonte
         self.titulo["bg"]=fundo
         self.titulo.pack()

class Criar_Entry:
    def __init__(self,root2,abcissa,ordenada,fonte,fundo,segredo):
         self.entry=Entry(root2,font=fonte)
         self.entry.place(x=abcissa,y=ordenada)
         if segredo:
             self.entry["show"]="*"

class Criar_Button:
    def __init__(self,root2,texto,fonte,fundo,comando):
         self.button=Button(root2)
         self.button["text"]=texto
         self.button["font"]=fonte
         self.button["bg"]=fundo
         self.button["command"]=comando
        
         self.button.pack(side=BOTTOM)
        
class Criar_RadioButton:
    def __init__(self,root2,fonte,fundo,texto,abcissa,ordenada,var):
         self.radiobutton=Radiobutton(root2)
         self.radiobutton["font"]=fonte
         self.radiobutton["bg"]=fundo
         self.radiobutton["text"]=texto
        #Revisar esta parte
        #self.radiobutton["variable"]=var
        
         self.radiobutton.place(x=abcissa,y=ordenada)

class Criar_Spinbox:
    def __init__(self,root2,origem,fim,abcissa,ordenada):
         self.spinbox=Spinbox(root2,from_=origem,to=fim)
         self.spinbox.place(x=abcissa,y=ordenada)
