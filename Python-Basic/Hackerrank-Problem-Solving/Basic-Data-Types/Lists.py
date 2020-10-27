#List
n=int(input())
l=[]
for i in range(0,n):
    s, *x = input().split()
    y=[]
    #print(s)
    if s=="insert":
        y = list(map(int, x))
        y = list(map(int, x))
        #print(y)
        l.insert(y[0],y[1])
    elif s=="print":
        print(l)
    elif s=="remove":
        y = list(map(int, x))
        l.remove(y[0])
    elif s=="append":
        y = list(map(int, x))
        l.append(y[0])
    elif s=="sort":
        l.sort()
    elif s=="pop":
        l.pop(-1)
    elif s=="reverse":
        l.reverse()
