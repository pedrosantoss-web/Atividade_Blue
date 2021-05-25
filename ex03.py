#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que
#  peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver 
# correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, 
# onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número
#  foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador 
# é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

from random import randint 
senha = 0 # CRIEI ESTA VARIAVEL PARA VALIDAR 
while senha != 3674:#WHILE  PARA CRIAR UMA ESTRUTURA DE REPETIÇÃO ATE QUE O USUARIO DIGITE OS NUMEROS CORRETOS
    senha = int(input(' senha por favor! : ')) #  INPUT PARA O USUARIO DIGITAR UMA SENHA SOMENTE COM NUMERO INTEIRO 1

print('Bem vindo ao jogo : ')   # APOS PASSAR PELA SENHA IRAR APARECER UMA MENSAGEM DE BOAS VINDAS      
comp = randint(0,10) # PARA GUARDAR O VALOR SORTEADO
print('acabei de pensar em um numero entre: 0,10')
print('Sera que vc consegue advinhar')
acertou = False # VARIAVEL  PARA Guardar quando o jogador acertar o palpite(false somente para validar)
palpite = 0 # para guardar quantidade de palpites
while not acertou:# while para repetir até o jogador aceertar o palpite
    jogador = int(input('qual o seu palpite ? '))# input para o jogador colocar os palpites
    palpite += 1 # para contar os palpites 
    if jogador == comp:# para quando o palpite do jogador for  igual ao numero sorteado termine 
        acertou = True
    else:#caso palpie for errado irá aparecer na tela numero maior ou menor
        if jogador < comp:  
            print('numero maior,tente novamete ')
        elif jogador > comp:# 
            print('numero menor, tente novamente ')

print(f'Você conseguiu com {palpite} palpites! Parabéns')

