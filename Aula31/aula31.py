'''
Formatando valores modificados  - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante ( float)
:.(NÚMERO)f - Quantidade de casas decimais ( float)
:(CARACTERE)(>ou < ou ^) ( QUANTIDADE)( TIPO - s,d ou f)

> - Esquerda
< - Direita
^ - Centralizar
'''

'''num_1 = 10
num_2 = 3
divisao= num_1/num_2
print(f'{divisao:.5f}')
#print('{:.2f}'.format (divisao))

nome= " Anderson Avila"
print(f'{nome:s}')   # ta convertendo para str
'''

'''num_1= 1
print(f'{num_1:0>10}')

num_2 = 1122
print(f'{num_2:1f}')
'''


nome = "Anderson Avila Torres"
nome_formatado = '{}'.format(nome)
print(nome_formatado)

nome = "Anderson Avila Torres"
print(nome.lower())  #tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  #Primeiras Letras Maisculas