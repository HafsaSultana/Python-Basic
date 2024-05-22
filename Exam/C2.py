#C2. Word_Frequency Count in File:
#fname = input("Enter file name: ")
#fh =open('A.txt')
fh=open('pg3807.txt')
l=[]
for i in fh:
    i=i.rstrip()
    z=i.split()
    s=''
    ss=''
    n=len(z)
    for j in z:
        s=''
        for k in j:

            if k==' ' or (k>='A' and k<='Z') or (k>='a' and k<='z') or (k>='0' and k<='9'):
                s+=k
        l.append(s)
l.sort()
d=dict()
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
for i,j in d.items():
    print(i,': ',j)
