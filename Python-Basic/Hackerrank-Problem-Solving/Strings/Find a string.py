def count_substring(string, sub_string):
    #Find a string
    s=string
    x=sub_string
    l=len(s)
    t=len(x)
    c=0
    for i in range(0,l):
        z=s[i:t+i]
        #print(z)
        if z==x:
            c=c+1
    return c

