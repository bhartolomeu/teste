from tkinter import *
from criar_widgets import *

def imprimir(root,texto,xy,fonte,fundo):
    mensagem=Criar_Label(root,texto,xy[0],xy[1]+30,fonte,fundo)
def _menu_():
    root=Tk()
    root["bg"]="LavenderBlush"
    xy=[]
    xy.append(1)
    xy.append(40)
    fonte=("Roboto",10)
    titulo=("Roboto",12)
    fundo="LavenderBlush"

    menu=Criar_Label(root,"Menu",180,0,fonte,fundo)

    #NOME
    nome=Criar_Label(root,"NOME",xy[0],xy[1],fonte,fundo)
    entrar_nome= Entry(root,font=fonte)
    entrar_nome.place(x=xy[0]+50,y=xy[1])
    #A seguinte classe está fora de uso
    #entrar_nome=Criar_Entry(root,xy[0]+50,xy[1],fonte,fundo,False)
    print(entrar_nome)

    #SENHA
    senha=Criar_Label(root,"SENHA",xy[0],xy[1]+30,fonte,fundo)
    entrar_senha=Criar_Entry(root,xy[0]+50,xy[1]+30,fonte,fundo,True)

    #Não dá para usar ".get()" pq o jeito que criamos o entry é por método, então quando usa-se essa função para capturar, o interpretador pensa que é um método que foi criado por nós.
    botao=Criar_Button(root,"INSERIR NOME",fonte,fundo,lambda:imprimir(root,entrar_nome.get(),xy,fonte,fundo))

    

##    #revisar esta parte
##    var = StringVar()
##    e=Criar_RadioButton(root,fonte,fundo,"Fêmea♀",xy[0],xy[1]+50,var.set("hello"))
##    e_=Criar_RadioButton(root,fonte,fundo,"Macho♂",xy[0],xy[1]+80,var.set("hello"))

    #f=Criar_Spinbox(root,1,31,xy[0],xy[1]+150)

    root.geometry('400x150')
    root.mainloop()

_menu_()
