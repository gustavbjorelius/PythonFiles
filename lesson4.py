"""
make a simple game 
* the computer guesses an int 1..100
* the user gets 5 tries to guess correct
* if the user guesses correctly then the computer outputs the number of tries it took
* if the user loses, then the tries run out, the program quits

do it iteratively 

"""
import random 

# init section
game_over = False 
number_of_attempts = 0
secret = random.randint(0,100)

if __name__ == "__main__": 
    print(f'The secret is {secret}')

while number_of_attempts < 5 and not game_over:
    user_guess = int(input('What is your guess? '))
    number_of_attempts += 1
    if user_guess == secret:
        game_over = True
        print(f'You won! it took {number_of_attempts} attempts!')
    else: 
        print(f'Nice try, you have {5 - number_of_attempts} attempts left!')
    if not game_over and number_of_attempts == 5:
        print('YOU DIED')
