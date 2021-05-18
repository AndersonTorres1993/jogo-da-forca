''''
While em Python - Aula 7
Utilizado para realizar ações enquanto uma condição for verdadeira.

Requisitos :  Entender condições e operadores
'''

'''x = 0
while x < 10:
    if x == 3:
        x = x +1
        break  #continue
    print(x)
    x = x +1
print('Acabou!')'''

'''x = 0 # coluna
y = 0 # linha

while x < 10:
    print(x)
    x +=1  #x = x + 1

print('Acabou!')'''


#x = 0 # coluna
#while x < 10:
#    y = 0  # linha
#    while y <5:
#     print(f'({x},{y})')
#      y += 1
#    x +=1  #x = x + 1

#print('Acabou!')
while True:
    print()
    num_1 = input('Digite um numéro: ')
    num_2 = input('Digite outro número: ')
    num_3= input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print(' Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int (num_2)

    if num_3 == '+':
        print(num_1 + num_2)
    elif num_3 == '-' :
        print(num_1- num_2)
    elif num_3 == '/':
        print(num_1/num_2)
    elif num_3 == '*':
        print(num_1*num_2)
    else:
        print('Operador Inválido.')