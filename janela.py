from tkinter import *
from criar_widgets import *

class Janelas:
	def __init__(self,fonte,fundo,xy,tela,titulo):
		#Esta é a variável da janela
		self.root = Tk()

		#esta é a corde fundo da janela
        self.root["bg"] = fundo     

    	#Este é o título
    	self.titulo=Criar_Label_Titulo(self.root,titulo,fonte,fundo))
    
    	#Este é o tamanho da janela
    	self.root.geometry(tela)
    	self.root.mainloop()

class Autenticar(Janelas):
	def __init__(self,fonte,fundo,xy,tela,titulo):
        super().__init__(fonte,fundo,xy,tela,titulo)
        self.nome=Criar_Label(self.root,"NOME",xy[0],xy[1],fonte,fundo)
        self.entrar_nome=Criar_Entry(self.root,xy[0]+50,xy[1],fonte,fundo,False)

        self.senha=Criar_Label(self.root,"SENHA",xy[0],xy[1]+30,fonte,fundo)
        self.entrar_senha=Criar_Entry(self.root,xy[0]+50,xy[1]+30,fonte,fundo,True)
        self.botao=Criar_Button(self.root,"INSERIR NOME",fonte,fundo,lambda:login(self.root,usuario,senha))

    def login(self,self.root,usuario,senha):
    	if usuario == "" and senha == "":
    		self.root.destroy()

    		#coco do dinossauro money do gagaca coco d dinossauro pamela linda maravilhosa de princesa gagaca seu cocozendo gagaca lindu chi linda bicosa é maravichosa coco de dinossaro mais eu sou um nenezim