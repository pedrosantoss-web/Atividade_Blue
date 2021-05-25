 #Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?"

investigação = []#até aqui criei uma lista e adicionei as pergutas que sera feita na invetigação,utilizei upper e strip para 
investigação.append(input('Telefonou para a vítima ? [S/N]')).strip().upper()[0]#deixar as letras maiusculas e retirar espaços para evitar dar erro 
investigação.append(input(' Esteve no local do crime? [S/N]')).strip().upper()[0]#e utizei[] na posição zero para por que irrei utilizar somente a primeira letra para validar mais abaixo.
investigação.append(input('Mora perto da vítima ? [S/N]')).strip().upper()[0]
investigação.append(input('Devia para a vítima ? [S/N]')).strip().upper()[0]
investigação.append(input('Já trabalhou com a vítima? [S/N]')).strip().upper()[0]
s =investigação.count('S')# Utilizei o count para contar as ocorrencias para utilizar essa informação no if para declarar a situação da pessoa
if s == 0 or s == 1: 
    print('Inocente!')
elif s == 2:
    print('Suspeita!') # if e elif para definição se caso for tal numero mostre na tela qual a situação da pessoa 
elif s == 3 or s == 4:
    print('Cúmplice!')
else:
    print('Assassino!')
    