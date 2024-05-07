titulo = 'Potenciação'
print(f'{titulo:^30}')

base = int(input("Qual a base: "))
exponencial = int(input("Qual a exponencial: "))

total = 1
if base < 1 or exponencial < 2:
    print("A base deve ser maior que 1 e o expo maior ou igual a 2")
else:
    for _ in range(exponencial):
        total = total * base

    print(f'{base} elevado {exponencial} é igual a {total}')

#com WHILE
total = 1
i = 1
if base < 1 or exponencial < 2:
    print("A base deve ser maior que 1 e o expo maior ou igual a 2")
else:
    while i <= exponencial:
        total =  total * base
       #ou
        total *=  base
        i += 1
    print(f'{base} elevado {exponencial} é igual a {total}')



