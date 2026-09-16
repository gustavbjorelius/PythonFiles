# https://bth.instructure.com/courses/7266/assignments/66769?module_item_id=257386
# Fibonacci-sekvensen kännetecknas av att varje nytt tal är summan av de två föregående talen.
# 1  2  3  4  5  6  7   8   9   10  11  12
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,

def fibonacci():
    a, b = 0, 1
    chosen_number = input('Calculate the fibonacci sequence up to this number: ')
    # validate input 
    while not chosen_number.isdigit():
        print('Vänligen mata in ett icke-negativt heltal!')
        chosen_number = input('Calculate the fibonacci sequence up to this number: ')
    for _ in range(int(chosen_number)):
        print(b, end="   ")
        a, b = b, a + b

fibonacci()