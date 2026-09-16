# https://bth.instructure.com/courses/7266/assignments/66769?module_item_id=257386
# Fibonacci-sekvensen kännetecknas av att varje nytt tal är summan av de två föregående talen.
# 1  2  3  4  5  6  7   8   9   10  11  12
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,

def fibonacci(validated_number):
    a, b = 0, 1
    for _ in range(int(validated_number)):
        print(b, end="   ")
        a, b = b, a + b

def validator_func(choosen_number):
    while not choosen_number.isdigit():
        print('Vänligen mata in ett icke-negativt heltal!')
        choosen_number = input('Calculate the fibonacci sequence up to this number: ')
    validated_number = choosen_number
    return validated_number


if __name__ == "__main__":
    chosen_number = input('Calculate the fibonacci sequence up to this number: ')
    validated_number = validator_func(chosen_number)
    fibonacci(validated_number)