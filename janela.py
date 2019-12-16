#!/usr/bin/python3
from tkinter import *
from criar_widgets import *

class Janelas:
    def __init__(self,fonte,fundo,titulo):
        #Esta é a variável da janela mãe
        self.root = Tk()

        #Esta é a cor de fundo da janela
        self.root["bg"]=fundo

        #Este é o título
        self.titulo=Criar_Label_Titulo(self.root,titulo,fonte,fundo)

class Menu(Janelas):
    def __init__(self,fonte,fundo,xy,tela,titulo):
        super().__init__(fonte,fundo,titulo)

        abaixar,alinhar=30,70

        self.bt_login=Criar_Button(self.root,"LOGIN",fonte,fundo,lambda:Autenticar(self.root, fonte, fundo, xy,"250x170","LOGIN"))

        self.bt_cadastrar=Criar_Button(self.root,"CADASTRO",fonte,fundo,lambda:Cadastrar(self.root,fonte, fundo,xy,"670x200","CADASTRO"))

        #Este é o tamanho da janela
        self.root.geometry(tela)


class Autenticar(Janelas):
    def __init__(self,janela_antiga,fonte,fundo,xy,tela,titulo):

        janela_antiga.destroy()

        super().__init__(fonte,fundo,titulo)

        abaixar,alinhar=30,70

        self.user=Criar_Label(self.root,"USUÁRIO",xy[0],xy[1],fonte,fundo)
        self.entrar_user=Criar_Entry(self.root,xy[0]+alinhar,xy[1],fonte,False)

        #Label e entrada da senha respectivamente
        self.senha=Criar_Label(self.root,"SENHA",xy[0],xy[1]+abaixar,fonte,fundo)
        self.entrar_senha=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+abaixar,fonte,True)

        #Botão que fará a mudança para uma nova tela
        self.botao=Criar_Button(self.root,"INSERIR NOME",fonte,fundo,lambda:Autenticar.login(self.root, self.entrar_user.entry.get(), self.entrar_senha.entry.get()))

        #Este é o tamanho da janela
        self.root.geometry(tela)
        self.root.mainloop()

    def login(root,usuario,senha):
        if usuario == "" and senha == "":
            print("Tudo certo, podemos fazer a próxima janela")
            #nova_janela=Cadastrar(root,["Roboto",10],"LavenderBlush",[1,40],('400x200'),"AUTENTICAR")

class Cadastrar(Janelas):
    def __init__(self,janela_antiga,fonte,fundo,xy,tela,titulo):
        #Adeus janela  antiga
        janela_antiga.destroy()

        #olá janela nova
        super().__init__(fonte,fundo,titulo)

        #As variáveis a seguir serão usadas para alinhar e abaixar cada widget
        abaixar,alinhar=30,150

        #Label e entrada do nome
        self.nome=Criar_Label(self.root,"NOME",xy[0],xy[1],fonte,fundo)
        self.entrar_nome=Criar_Entry(self.root,xy[0]+alinhar,xy[1],fonte,False)
        
        var=StringVar()

        self.genero=Criar_Label(self.root,"GÊNERO",xy[0],xy[1]+abaixar,fonte,fundo)

        self.feminino=Criar_RadioButton(self.root,
                                        fonte,
                                        fundo,
                                        "FEMININO",
                                        xy[0]+alinhar,
                                        xy[1]+abaixar,
                                        var,
                                        "FEMININO")

        self.masculino=Criar_RadioButton(self.root,
                                        fonte,
                                        fundo,
                                        "MASCULINO",
                                        xy[0]+alinhar+100,
                                        xy[1]+abaixar,
                                        var,
                                        "MASCULNO")

        self.feminino=Criar_RadioButton(self.root,
                                        fonte,
                                        fundo,
                                        "OUTRO",
                                        xy[0]+alinhar+213,
                                        xy[1]+abaixar,
                                        var,
                                        'OUTRO')
        #self.entrar_genero=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+abaixar,fonte,False)

        #Abaixar widgets mais 30 pixels
        abaixar+=30

        self.data_nascimento=Criar_Label(self.root,"DATA NASCIMENTO",xy[0],xy[1]+abaixar,fonte,fundo)
        self.entrar_dia=Criar_Spinbox(self.root,1,31,xy[0]+alinhar,xy[1]+abaixar,5)
        self.entrar_mes=Criar_Spinbox(self.root,1,12,xy[0]+alinhar+60,xy[1]+abaixar,5)
        self.entrar_ano=Criar_Spinbox(self.root,1900,2019,xy[0]+alinhar+120,xy[1]+abaixar,5)

        #Abaixar widgets mais 30 pixels
        abaixar+=30

        self.botao_cadastrar=Criar_Button(self.root,
            "CADASTRAR",
            fonte,
            fundo,
            lambda:Cadastrar.salvar(self.entrar_nome.entry.get(),
                                    var.get(),
                                    self.entrar_dia.spinbox.get(),
                                    self.entrar_mes.spinbox.get(),
                                    self.entrar_ano.spinbox.get()))

        self.root.geometry(tela)
        self.root.mainloop()

    def salvar(nome,genero,dia_nascimento,mes_nascimento,ano_nascimento):
        a=[nome,genero,[dia_nascimento,mes_nascimento,ano_nascimento]]
        print("Nome: ",a[0])
        print("Genero: ",a[1])
        print("Data de Nascimento: ",a[2][0]+"/"+a[2][1]+"/"+a[2][2])

