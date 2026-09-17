summa = 0
antal_tal = 0
maxi = 0
mini = 0

user_input = float(input("Mata in ett tal: "))

maxi = user_input
mini = user_input

while user_input != 0:

    if user_input > maxi:
    maxi = user_input
    if user_input < mini:
        mini = user_input
        antal_tal += 1

    summa += user_input

user_input = float(input("Mata in ett tal: "))

medelvärde = (summa - maxi - mini)/(antal_tal - 2)

print(medelvärde)