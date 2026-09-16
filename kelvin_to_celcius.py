kel = input('What is the temperature in Kelvin? ')
if kel.isdigit():
    cel = kel - 273.15
    print(cel)
else:
    print('Please input a number! ')
    
