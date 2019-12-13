from tkinter import *
from criar_widgets import *

class Janelas:
  def __init__(self,fonte,fundo,xy,tela,titulo,original):
    #Caso seja a janela mãe
    if original:
      #Esta é a variável da janela mãe
      self.root = Tk()

      #Caso seja uma janela filha
    else:
      #Esta é a variável da janela filha
      self.root= Toplevel() 

    #Esta é a cor de fundo da janela
    self.root["bg"]=fundo
    #Este é o título
    self.titulo=Criar_Label_Titulo(self.root,titulo,fonte,fundo)
    #Este é o tamanho da janela

class Autenticar(Janelas):
  def __init__(self,fonte,fundo,xy,tela,titulo):
    super().__init__(fonte,fundo,xy,tela,titulo,True)

    abaixar,alinhar=30,70

    self.user=Criar_Label(self.root,"USUÁRIO",xy[0],xy[1],fonte,fundo)
    self.entrar_user=Criar_Entry(self.root,xy[0]+alinhar,xy[1],fonte,fundo,False) 

    #Label e entrada da senha respectivamente
    self.senha=Criar_Label(self.root,"SENHA",xy[0],xy[1]+abaixar,fonte,fundo)
    self.entrar_senha=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+abaixar,fonte,fundo,True)

    #Botão que fará a mudança para uma nova tela
    self.botao=Criar_Button(self.root,"INSERIR NOME",fonte,fundo,lambda:login(self.root,self.entrar_user.entry.get(),self.entrar_senha.entry.get()))

    #Este é o tamanho da janela
    self.root.geometry(tela)
    self.root.mainloop()

  def login(self,usuario,senha):
    if usuario == "" and senha == "":
      #print("Tudo certo, podemos fazer a próxima janela")
      nova_janela=Cadastrar(self.root,["Roboto",10],"LavenderBlush",[1,40],('400x150'),"AUTENTICAR")

class Cadastrar(Janelas):
  def __init__(self,janela_antiga,fonte,fundo,xy,tela,titulo,original):
    #Adeus janela antiga
    janela_antiga.destroy()
    #olá janela nova
    super().__init__(fonte,fundo,xy,tela,titulo,False)

    #As variáveis a seguir serão usadas para alinhar e abaixar cada widget
    abaixar,alinhar=30,25

    #Label e entrada do nome
    self.nome=Criar_Label(self.root,"NOME",xy[0],xy[1],fonte,fundo)
    self.entrar_nome=Criar_Entry(self.root,xy[0]+alinhar,xy[1],fonte,fundo,False)
    
    #Abaixar widgets mais 30 pixels
    abaixar+=30

    self.genero=Criar_Label(self.root,"GÊNERO",xy[0],xy[1]+abaixar,fonte,fundo)
    self.entrar_genero=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+abaixar,fonte,fundo,False)

    #Abaixar widgets mais 30 pixels
    abaixar+=30
    
    self.data_nascimento=Criar_Label(self.root,"DATA NASCIMENTO",xy[0],xy[1]+abaixar,fonte,fundo)
    self.entrar_data_nascimento=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+abaixar,fonte,fundo)

    self.idade=Criar_Label(self.root,"IDADE",xy[0],xy[1]+abaixar,fonte,fundo)
    self.entrar_idade=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+abaixar)

    self.botao_cadastrar=Criar_Button(self.root,"CADASTRAR",fonte,fundo,salvar)

    self.root.geometry(tela)
    self.root.mainloop()

  def salvar():
    print("O botao funciona!!!")
