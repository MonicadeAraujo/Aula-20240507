titulo = 'Contagem de Vogais'
print(f'{titulo:^30}')

frase =  input("Qual a frase pra contar vogais: ").upper()

vogais, consoantes, espacos = 0, 0, 0
for palavra in frase.split():
    print(palavra)

for letra in frase:
    if letra in 'aeiouAEIOUáéíóú':
        vogais += 1
    elif letra == ' ':
        espacos += 1
else:
    consoantes += 1


print(f'A frase: {frase} tem {vogais} vogais, {consoantes}, consoantes, {espacos}, espacos   ')



