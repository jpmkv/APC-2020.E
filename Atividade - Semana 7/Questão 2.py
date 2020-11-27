car_list = []
consum_list = []

while len(car_list) < 5:
    car_list.append(input('Digite o nome do carro: '))
    consum_list.append(float(input('Digite o consumo do carro (km/litro): ')))
    print('Dados registrados!\n')

kilom_t = 1000
gas_value = 2.25
cars = ''

for a, b in enumerate(car_list):
    print(f'Veiculo {a+1}')
    print(f'Nome: {b}')
    print(f'Km por litro: {consum_list[a]}\n')

    consum_litr = round(kilom_t/consum_list[a], 2)
    cars += f'O {b} consome {consum_litr}L e custará $R{round(consum_litr*gas_value, 2)} caso venha fazer {kilom_t}km\n'

print()
print(f'O {car_list[consum_list.index(max(consum_list))]} é o carro mais económico.')
print()
print(cars)
