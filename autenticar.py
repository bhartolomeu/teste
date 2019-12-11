from tkinter import *
from criar_widgets import *
class primeira_janela:

    def imprimir(root,texto,xy,fonte,fundo):
        mensagem=Criar_Label(root,texto,xy[0],xy[1]+80,fonte,fundo)
    
    def menu(fonte,fundo,xy):
        root=Tk()
        root["bg"]=fundo
       
        #Título da janela
        titulo=Criar_Label_Titulo(root,"MENU",fonte,fundo)

        #NOME
        nome=Criar_Label(root,"NOME",xy[0],xy[1],fonte,fundo)

        #A seguinte classe está fora de uso
        entrar_nome=Criar_Entry(root,xy[0]+50,xy[1],fonte,fundo,False)

        #SENHA
        senha=Criar_Label(root,"SENHA",xy[0],xy[1]+30,fonte,fundo)
        entrar_senha=Criar_Entry(root,xy[0]+50,xy[1]+30,fonte,fundo,True)

        botao=Criar_Button(root,"INSERIR NOME",fonte,fundo,lambda:imprimir(root,entrar_nome.entry.get(),xy,fonte,fundo))

        root.geometry('400x150')
        root.mainloop()

##    #revisar esta parte
##    var = StringVar()
##    e=Criar_RadioButton(root,fonte,fundo,"Fêmea♀",xy[0],xy[1]+50,var.set("hello"))
##    e_=Criar_RadioButton(root,fonte,fundo,"Macho♂",xy[0],xy[1]+80,var.set("hello"))

    #f=Criar_Spinbox(root,1,31,xy[0],xy[1]+150)