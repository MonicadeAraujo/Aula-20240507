titulo = 'Estado onde nasceu'
print(f'{titulo:^30}')

estado = input('Informe o codigo do estado onde nasceu: ' ).upper()

# if estado == 'RJ':
#     print("Carioca")
# elif estado == 'SP':
#     print("Paulista")
# elif estado == 'MG':
#     print("Mineiro")
# elif estado == 'BA':
#     print("Bahiano")
# elif estado == 'CA':
#     print("Cearense")
# else:
#     print("Outros estados")

#outra maneira
if estado in ('SP', 'Sao Paulo', 'São Paulo'):
    print('Paulista')
elif estado == 'RJ':
    print('Carioca')
else:
    print("Outros estados")
