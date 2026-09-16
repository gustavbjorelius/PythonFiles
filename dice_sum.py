import random
# ask the user how many die throw 
n_throw = int(input('Hur många kast ska göras? (avsluta genom att skriva q)'))

# the user gets asked again after completion so perhaps we can use a while loop
while n_throw != "q": # comment 
    x = 0
    # use a loop to simulate number of throws
    for i in range(0, int(n_throw)): 
        # sum them 
        x += random.randint(1,6)
    print('Summan av de ', n_throw, ' kasten är', x)
    n_throw = input('Hur många kast ska göras? (avsluta genom att skriva q)')
