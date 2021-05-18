'''
*Criar variáveis para nome (str), idade (int)
*altura (float) e peso (float) de uma pessoa
*Criar variável com ano atual (int)
*Obter o ano de nascimento da pessoa ( baseada nda idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando  F-strings( com as chaves)
'''

nome = 'Luiz'
altura = 1.8
peso =80.5
imc= peso/altura**2
idade = 32
ano_atual = 2019
nascimento = ano_atual-idade

print (f'{nome} tem {idade} anos e {altura} de altura.')
print (f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print (f'{nome} nasceu em {nascimento}.')
