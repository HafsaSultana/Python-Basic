#List Comprehensions
x=int(input())
y=int(input())
z=int(input())
n=int(input())
a=list()
l=list()
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if (i+j+k)==n:
                continue
            a.append(i)
            a.append(j)
            a.append(k)
            l.append(a)
            a=[]
print(l)
                
