# palavra1 =
# palavra2 =
#
# frase = palavra1 + ' ' + palavra2
# print(frase)
#
# fraseinversa =  palavra2 + '' + palavra1
# print(fraseinversa)

titulo = 'Palindromo'
print(f'{titulo:^30}')
#REVIVER, MONICA

palavra = input("Qual a palavra: ")
reversa = " "
resp = 's'

while resp in ('s', 'sim', 'y', 'yes', 'sí'):
    palavra = input("Qual a palavra: ")
    reversa = " "
    resp = 's'
    for letra in palavra:
        reversa = letra + reversa
    if palavra == reversa:
        print(f'A palavra é {palavra}" é palindrome')
    else:
        print(f' A palavra {palavra} não é palindrome')
resp = input('Quer continuar a brincar? ').lower()

