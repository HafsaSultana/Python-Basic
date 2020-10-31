n = int(input())
for i in range(0, n):
    a, b = list(map(str, input().split()))
    try:
        a = int(a)
        b = int(b)
        print(int(a / b))
    except:
        if b == 0 :
            print("Error Code: integer division or modulo by zero")
        elif type(a) is str:
            print("Error Code: invalid literal for int() with base 10: '" + str(a) + "'")
        elif type(b) is str:
            print("Error Code: invalid literal for int() with base 10: '" + str(b) + "'")
