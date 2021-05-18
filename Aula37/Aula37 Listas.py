'''
Listas em Python
fatiamento
append, insert , pop, del, clear, extend, +
min, max
range
'''
#         0   1   2    3   5
# lista = ['A','B','C', 'D','E']
#  -      5   4    3    2   1
# string = 'ABCDE'
# print(string[1])
#
# l2 = ['String',True, 10, -20.5]
#
# for elem in l2:
#     print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')
secreto = 'perfume'
digitadas= []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhuhuuuuu, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Affffzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            print(secreto_temporario)
            secreto_temporario += letra_secreta
            print(secreto_temporario)
        else:
            secreto_temporario += '*'


    if secreto_temporario == secreto:
        print(f'Que legal, você ganhou!!!!  A palavra era {secreto_temporario}.')
        break
    else:
        print(f' A palavra secreta está assim : {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()