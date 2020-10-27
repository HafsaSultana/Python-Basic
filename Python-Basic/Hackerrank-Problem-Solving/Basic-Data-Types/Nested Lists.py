#Nested Lists
d={}
l=list()
a=list()
n=int(input())
for i in range (0,n):
    x=input()
    y=float(input())
    d[x]=y
#print("dicnonany: ",d)
for i,j in d.items():
    l.append(j)
#print("List : ",l)
l.sort()
#print("SortList : ",l)
c=l[0]
for i in l:
    if c==i:
        continue
    else:
        z=i
        break
for i,j in d.items():
    if z!=j:
        continue
    else:
        a.append(i)
a.sort()
for i in a:
    print(i)
