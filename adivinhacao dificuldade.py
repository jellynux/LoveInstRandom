from cmath import sqrt
from logging.handlers import TimedRotatingFileHandler
from random import random

import random
# Acima, eu importei um número aleatorio, e vou puxar a variável abaixo!
print(''''
        ***********************************
        Olá, bem-vindo ao jogo de adivinhação!!!
        **********************************''')

                #round= arredondar/ o resto determina o valor
numero_secreto = round(random.randrange(1,1001))
rodada = 1



print('Ecolha a dificuldade do desafio!')
print('(1) Fácil  (2) Médio  (3) Difícil')

nivel = int(input('Defina o nível:  '))

if (nivel == 1):
    tentativaescolhida = 30
elif (nivel == 2):
    tentativaescolhida = 20
elif (nivel == 3):
    tentativaescolhida = 10



nivel = tentativaescolhida


while (rodada <= tentativaescolhida):
    print ('Tentativa {} de {}'.format(rodada, tentativaescolhida)) 
    #A parte do imput, serve para podermos interagir (Responder) e salvar valores.
    chute = int(input('Digite o seu número :  '))
    #O print, vai mostrar e apresentar o número que eu coloquei
    print ('Você digitou', chute)

    #O int é muito importante, pois ele converte o valor (Sring > Número ou VSVS)
    
    acertou = numero_secreto == chute 
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (acertou):
        print ("Parabéns, você acertou!!!")
        print ('Fim de jogo, obrigado!')
        break

    else : 
        if(maior): 
            print ('O seu chute foi maior do que o número secreto!')
        elif (menor):
            print ('O seu chute foi menor.')

    rodada = rodada + 1

   
