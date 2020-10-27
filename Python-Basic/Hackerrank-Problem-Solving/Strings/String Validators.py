#String Validators
s=input()
n=0
a=0
d=0
l=0
u=0
for i in s:
    if i.isalnum()==True:
        n=1
    if i.isalpha()==True:
        a=1
    if i.isdigit()==True:
        d=1
    if i.islower()==True:
        l=1
    if i.isupper()==True:
        u=1
if n==1:
    print("True")
else:
    print("False")
if a==1:
    print("True")
else:
    print("False")
if d==1:
    print("True")
else:
    print("False")
if l==1:
    print("True")
else:
    print("False")
if u==1:
    print("True")
else:
    print("False")
