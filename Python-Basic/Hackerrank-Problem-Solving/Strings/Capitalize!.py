# Complete the solve function below.
def solve(s):
    #Capitalize!
    z=''
    if(s[0]>='a') and (s[0]<='z'):
        x=s[0].upper()
        z+=x
    else:
        z+=s[0]
    for i in range (1,len(s)):
        if (s[i-1]==' ')and((s[i]>='a') and (s[i]<='z')):
            x=s[i].upper()
            z+=x
            #print(z)
            i=i+1
        else:
            z+=s[i]
    return z


