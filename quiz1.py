# explain what, and why

def is_positive(n):
    if n > 0:
        print("Value is positive", end=" ")
        return True
    # what does the end= " " do? 
    print("Value is negative", end=" ") 
    return False

is_positive(-2) and is_positive(2)
