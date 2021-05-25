#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

valor1 = int(input('Digite o primeiro valor:\n'))
valor2 = int(input('Digite o segundo valor:\n '))  # sera pedido dois valores inteiros a o usuario  
soma = valor1 + valor2
mult = valor1 * valor2   # variaveis que ira realizar contas e guardar o resultado e variaveis que irie guardar o resultado das validaçções em baixo 
div = valor1 / valor2
par = soma % 2
maior = 0
print(f'{valor1} + {valor2} = {soma}')
print(f'{valor1} * {valor2} = {mult}') # ira mostrar  na tela o resultado das contas 
print(f'{valor1} / {valor2} = {div}')
print('---'*30)#
if (valor1 > valor2 ):
      maior = valor1                # usando if para validar informações dos calculos feito acima
elif (valor2 > valor1):             # se caso o resultado for igual ao que eu quero que ele mostre ele ira mostra na tela
   maior = valor2
   print(f'o maior valor é {maior}')
if soma == 0:
   print(f'o vador da soma e {par}')
if (mult >= 40) :
   print(f' O resultado da multiplicação foi maior que 40, \n por isso o valor sera dividido pelo resultado da divisão:\n {mult/div} ')






   
