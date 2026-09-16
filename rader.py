# hur många rader skrivs ut från denna kod? 

def add(x, y):
    return x+y

def mult(x, y):
    print(x*y)
    # implicitly return None here 
    # all Python functions return a value
    # if no return statement is given, Python returns None automatically    
    # so this func prints to the terminal, but the function returns None

add(1,2) # 0 
print(add(2,3)) # 1
mult(3,4) # 2 
print(mult(4,5)) 
# first it calls the function mult(4,5) that prints 20
# then as that function returns None, python executes 'print(None)', which out: None
# so in total it's 4 lines 