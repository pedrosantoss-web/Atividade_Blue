# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
#  Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário.
#  Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar.
#  Considere que o trabalhador deve contribuir por 35 anos para se aposentar
from datetime import date # importei date da biblioteca datetime  para me ajuda a utilizar o ano atual
ano = date.today().year
func = dict()                          # criei u discionario vazio e pedi ao usuario atravez de input dados trabalhistas 
func['Nome'] = input('Nome:\n ')
nascimento = int(input('Ano de nascimento:\n ')) 
idade = ano - nascimento   # criei estas variaveis para  que eu consiga fazer e guardar contas 
func['idade'] = idade
func['CTPS'] = int(input('Nº Carteira de trabalho caso não possua digite[0]:\n '))
if func['CTPS'] != 0:         # caso não tenha carteira de trabalho o digitando zero o programa sera encerrado
    func['anoContratacao'] = int(input('Ano de contratação:\n '))
    func['Salário'] = int(input('Salário: '))
    aposentadoria = (func['anoContratacao'] + 35) - ano   # algumas contas utilizando variaveis que fiz la em cima para saber alguns
    aposentado = idade + aposentadoria
    print(f'Você vai estar com {aposentado} anos quando aposentar \nfalta {aposentadoria} anos para você aposentar.')# mostrar na tela o resultado 
    