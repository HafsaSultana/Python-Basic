def split_and_join(line):
    x=''
    for i in line:
        if i==' ':
            x+='-'
        else:
            x+=i

    return x

