def print_formatted(number):
    # your code goes here
    #String Formatting
    n=number
    #String Formatting
    if n==1:
        print(1,1,1,1)
    else:
        w=[]
        x=[]
        y=[]
        z=[]
        for i in range(1,n+1):
            w.append(i)
            x.append(oct(i))
            y.append(hex(i))
            z.append(bin(i)) 
            #print(i,x[2:],y[2:],z[2:])
            #print(i,oct(i),hex(i),bin(i))
        #space count
        s=z[n-1]
        l=len(s)
        ss=''
        for i in range(2,l-2):
            ss+=' '
        #print 
        for i in range(0,n):
            a=str(w[i])
            b=str(x[i])
            c=str(y[i])
            d=str(z[i])
            e=int(a)
            
            #print(a,ss,b[2:],ss,c[2:],ss,d[2:])
            print(a.rjust(l-2,' '),b[2:].rjust(l-2,' '),(c[2:].upper()).rjust(l-2,' '),d[2:].rjust(l-2,' '))
        #print("{:< ld}".format(e))
        return 

