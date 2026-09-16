
alt = """ ----------- ORDER -----------
1. Öl (35 SEK)
2. Vin (40 SEK)
3. Kaffe (25 SEK)
4. Te (20 SEK)
5. Äppeljuice (30 SEK))
-------------------------"""

def get_and_verify_input():
    menu = input("Mata in din order: ") # this needs to be a string else it's going to be hard to che
    for character in menu: 
        if character not in '12345':
            print('Endast siffror mellan 1-5 är tillåtna.')
            return get_and_verify_input()
    return menu 

def calculate_sum(menu): # do i have to input menu here too? 
    # assume order = 123 
        # first iteration: sum = 0, character = 1, sum += 35
        # second iteration: sum = 35, character = 2, sum += 40
        # third iteration : sum = 75, character = 3, sum += 25
        # sum = 100 in the end 
    total = 0
    for character in menu:
        if character == '1':
            total += 35
        elif character == '2':
            total += 40
        elif character == '3':
            total += 25
        elif character == '4':
            total += 20
        elif character == '5':
            total += 30
    # print(sum, type(sum), 'from calculate_sum func')
    return total 

def add_percentage(total, percentage=12): 
    return total * (1 + percentage / 100)

def add_tip(sum_and_vat):
    dricks = input('Hur många procent dricks will du lägga till? ')
    while not dricks.isdigit():
        dricks = input(' Hur många procent dricks will du lägga till? ')
    dricks = float(dricks)
    print(f'Notan blir {sum_and_vat + (sum_and_vat * dricks/100):.2f} kr. Välkommen åter!')

def main():
    print(alt)
    menu = get_and_verify_input()
    total = calculate_sum(menu)
    sum_and_vat = add_percentage(total, percentage=12)
    add_tip(sum_and_vat)

if __name__ == "__main__":
    main()