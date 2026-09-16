# Implementera en funktion max2(num1, num2) som tar emot två tal som argument och returnerar det största av dem. 

def max2():
    num = input('Input two numbers, separated with a space: ')
    list = num.split(" ")
    num1, num2 = int(list[0]), int(list[1])
    if num1 > num2:
        print(num1, 'is greater than', num2)
    else: 
        print(num2, 'is greater than', num1)
 

max2()