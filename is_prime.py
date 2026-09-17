from math import sqrt

def is_prime(n):
    '''
    input: integer n
    output: True if n is prime, else False 
    algo: 
        pass n to function
        return false as soon as divisor found 
        return true only after all divisors under sqrt(n)+1 checked
    '''
    if n <= 1: 
        return False

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0: 
            return False

    return True

print(is_prime(11))