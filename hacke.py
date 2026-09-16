''' this is supposed to: 
    have a list of integers
    put all the even ones in the beginning of the list
    put all the odd in the end of the list
    so that is to rearrange the list? 
    or is  it to create then rearrange? 


    there is no function call? 
    where is the list? I can't see any list anywhere 
    
    lessons learned 
        1. simulate the script from start to end in your head 
        2. simulate a trivial case 
'''
def even_first(x):
# we assume that this function gets called with the input of a list
    i = -1
    # assigns initial value to -1 to i 
    j = len(x)  
    # assigns init value to j
    # 0 <= j <= n 
    # the list length cannot be less than 0
    # Can a list have length 0? yes: y = []; in:len(y) out:0
    while j != i+1: 
    # if the list is empty -> len(x) -> j = 0 and this loop doesn't start
    # so the list must be non-empty, only then the while loop starts
    # while 0 != i + 1: 
    # while 0 != -1 + 1: 
    # while 0 != 0: 
    # while False: 
        if x[i + 1] % 2 == 0: # if x[-1 + 1] % == 0: 
        # asks, at the index of i + 1, is that int even? 
            i = i + 1
            # if above true, then add 1 to i 
        else:
        # if no other condition is true, then do the below 
            x[i], x[j] = x[i], x[j] 
            # why ? it assigns the values to itself? 
            # perhaps it all makes sense when I  do this 
            # I should have tested the code right away as I got an index error in the location where i need to change the code. 
            j = j - 1
            # for each iteration of this loop, ass take the initial length of the list x, and subtract it 
            # j = len(list from user) -1 
            # this goes to 0 

even_first([1,2,3,4,5,6,7])
