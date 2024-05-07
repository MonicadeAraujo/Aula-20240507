titulo = 'Menor, Intermediario, Maior'
print(f'{titulo:^30}')

n1 = int(input("Digite o primero numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

print(f'Os numeros: {n1} , {n2}. {n3}' , end= "")

if n1 > n2:
    t = n1
    n1 = n2
    n2 = t

if n1 > n3:
    t = n1
    n1 = n3
    n3 = t

if n2 > n3:
    t = n2
    n2 = n3
    n3 = t

print(f'são menor: {n1} , inter: {n2}. maior: {n3}')

