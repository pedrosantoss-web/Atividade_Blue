'''04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no
  formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.'''


def mes_p_Extenso(): 
    mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
           'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    dd = int(input('digite o dia [DD] :\n '))
    mm = int(input('digite o mês [MM] :\n '))
    ano = int(input('digite o ano [AAAA]:\n '))
    print(f'A data que você digitou : {dd}/{mm}/{ano}')
    print(f'{dd} DE {mes[mm -1]}  {ano}')


mes_p_Extenso()