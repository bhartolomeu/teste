#!/usr/bin/python3
import os
#import commands

voltar=True
while voltar:
    espaco=" "*45+"_"*70
    print(espaco)
    titulo=input("Por favor insira um título de até 70 dígitos:")
    texto=input("Insira o corpo do texto: ")
    
    contar=0
    for letra in titulo:
        contar+=1
    
    if contar > 70:
    
        print("Título muito grande, insira um menor.")
        voltar=True
    else:
        
        resto=" "*(70-contar)
        titulo=titulo+resto
        
        comentario=titulo+texto
        print("-"*4)
        print("Este é o comentário:",comentario)
        print("-"*4)
        
        comando="sudo git commit -m '"+comentario+"'"
        print(os.system(comando))
        print("-"*4)
        voltar=False

