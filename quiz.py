# i don't get this 
def if_test3(n):
    if n > 2:
        # doesn't this print fall 1 AND go down the control flow? 
        print("Fall 1") # so this is skipped if the below condition is ok?
        if n >= 0: # if n<2, n>=0, then the above print is skipped? 
            print("Fall 2")
    else:
        print("Fall 3")

if_test3(0)
