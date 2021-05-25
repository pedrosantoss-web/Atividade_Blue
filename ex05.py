# Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.
frase = str(input('digite uma frase: \n')).upper()
vogal = 0
def tiraVogal():
    print (frase)
    

for i in frase:
  if i in 'AEIOU':
    vogal +=1
for i in frase:
  if i in 'AEIOU':  
      frase = frase.replace(i,'') 
print(f'Nesta frase tem : \n {vogal}' )      
print(f'A frase sem as vogais ficou assim : \n {frase}')
tiraVogal()
         

