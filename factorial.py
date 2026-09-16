''' a factorial calculator '''
number = int(input('Nummer? '))
result = 1 

for i in range(number, 0, -1):
    result *= i

print(result)