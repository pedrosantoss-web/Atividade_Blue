#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.
frase = str(input('digite a frase:\n ')).upper()# PEDINDO  UMA FRASE AO USUARIO
vogais = 0 # CRIEI  UMA VARIAVEL PARA GUARDAR A QUANTIDADE QUE DE VOGAIS QUE VAI APRESENTAR NA FRASE 
for l in frase: 
    if l in 'AEIOU': # ESSE FOR E PARA QUE EM CADA VOLTA ELE IDENTIFICA SE TEM ALGUMA VOGAL
        vogais += 1 # SE TIVER ELE IRA GUARDAR NA VARIAVEL VOGAIS
print(f'Nesta frase tem : \n {vogais}' ) 
for l in frase:
  if l in 'AEIOU': # ESSE FOR É PARA QUE EM CADA VOLTA ELE CONSIGA IDENTIFICAR AS VOGAIS 
      frase = frase.replace(l,'') # USEI O REPLACE PARA TROCAR AS VOGAIS POR ESPAÇOS FECHADOS 
print(f'A frase sem as vogais ficou assim : \n {frase}')       
