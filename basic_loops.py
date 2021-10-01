monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(round(temperature))

#for letter in 'hello':
#    print(letter)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int):
        print(color)

for color in colors:
    if (isinstance(color, int)) and (color > 50):
        print(color)
