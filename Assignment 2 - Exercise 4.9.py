def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print('Celcius', '\t','Fahrenheit')

for celsius in range(101):
    print(f'{celsius:10}{fahrenheit(celsius):10.1f}')