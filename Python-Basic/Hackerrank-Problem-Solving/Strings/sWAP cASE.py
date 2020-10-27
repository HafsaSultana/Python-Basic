def swap_case(s):

    x=''
    for i in s:
        if (i.isupper()) == True: 
            x+=(i.lower()) 
        elif (i.islower()) == True: 
            x+=(i.upper())
        else:
            x+=i

    return x
