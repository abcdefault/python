#Encriptador e Decriptador de mensagem
#CIFRA DE CESAR

import os

def limparTela():
    x = os.name
    if(x == "posix"):
        os.system('clear')
    else:
        os.system('cls')

def encriptar(frase, key): 
    for i in range(0, len(mensagem), +1): #Percorre toda a frase
        aux = ord(frase[i]) + key #Converte o caractere para inteiro e adiciona a chave
        aux = chr(aux) #Converte o inteiro criptografado e transforma em caractere novamente
        print(aux, end="") #Exibe o caractere ja criptografado na tela
    print("\n")
    return 0


def decriptar(frase, key):
    key *= -1 #Multiplica a chave por (-1) fará que ela faça o inverso do encriptador.
    for i in range(0, len(frase), +1): #Percorre toda a frase
        aux = ord(frase[i]) + key #Converte o caractere para inteiro e adiciona a chave
        aux = chr(aux) #Converte o inteiro criptografado e transforma em caractere novamente
        print(aux, end="") #Exibe o caractere ja criptografado na tela
    return 0
    print("\n")

print("-=" * 40)
mensagem = str(input("Digita a mensagem: "))
mensagem = mensagem.strip()

limparTela()

print("-=" * 40)
print("Digite 1 para encriptar e 2 para decriptar")
x = int(input("O que deseja fazer? ").strip())
print("-=" * 40)
limparTela()

chave = int(input("Digite a chave: "))


if (x == 1):
    encriptar(mensagem, chave)
else:
    decriptar(mensagem, chave)
