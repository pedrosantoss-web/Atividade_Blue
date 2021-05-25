#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[],[]] # lista composta para guardar numeros pares e impares 
num = 0 # variavel para guardar os numeros que o usuario vai colocar durante as voltas do for 
for c in range(1,8): # for para repetir a pergunta 7 vezes 
    num = int(input(f'Digite o {c}º numero:\n'))
    if num % 2 == 0:       # nesta parte o if ira separar par e impar se caso for par vai para um lista se não vai para outra 
        lista[0].append(num)
    else:                      
        lista[1].append(num)
print('')
lista[0].sort()   # para organizar as listas de forma crescente 
lista[1].sort()
print(f'os numeros pares digitados foram : \n {lista[0]}')   # mostrar na tela o resultado
print(f'os numeros impares digitados foram: \n {lista[1]} ')     
