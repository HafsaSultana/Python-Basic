#Find the Runner-Up Score!
n=int(input())
l=[]
x=list(map(int, input().split()))
x.sort()
l=len(x)
ans=0
z=x[l-1]
for i in range(l-1,-1,-1):
    if x[i]==z: continue
    ans=x[i]
    break
print(ans)
