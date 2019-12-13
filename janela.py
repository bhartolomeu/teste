from tkinter import *
from criar_widgets import *

class Autenticar:
  def __init__(self,fonte,fundo,xy,tela,titulo,original):
    #Caso seja a janela mãe
    if original:
      #Esta é a variável da janela mãe
      self.root = Tk()

      #Caso seja uma janela filha
    else:
      #Esta é a variável da janela filha
      self.root= Toplevel()  

      #Label e Entrada do nome respectivamente
    self.nome=Criar_Label(self.root,"NOME",xy[0],xy[1],fonte,fundo)
    self.entrar_nome=Criar_Entry(self.root,xy[0]+50,xy[1],fonte,fundo,False)  

    #Label e entrada da senha respectivamente
    self.senha=Criar_Label(self.root,"SENHA",xy[0],xy[1]+30,fonte,fundo)
    self.entrar_senha=Criar_Entry(self.root,xy[0]+50,xy[1]+30,fonte,fundo,True)

    #Botão que fará a mudança para uma nova tela
    self.botao=Criar_Button(self.root,"INSERIR NOME",fonte,fundo,lambda:login(self.root,self.entrar_nome.entry.get(),self.entrar_senha.entry.get()))

    def login(self,usuario,senha):
      if usuario == "" and senha == "":
        print("Tudo certo, podemos fazer a próxima janela")
        #self.root.destroy()

class Janelas(Autenticar):
  def __init__(self,fonte,fundo,xy,tela,titulo,original):
    super().__init__(fonte,fundo,xy,tela,titulo,original)
    
    #Esta é a cor de fundo da janela
    self.root["bg"]=fundo
    #Este é o título
    self.titulo=Criar_Label_Titulo(self.root,titulo,fonte,fundo)
    #Este é o tamanho da janela
    self.root.geometry(tela)
    self.root.mainloop()


