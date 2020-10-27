from pip._vendor.distlib.compat import raw_input

#main code
def is_leap(year):
    x = year

    if (x % 4) == 0:
        if (x % 100) == 0:
            if (x % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

        return leap


year = int(raw_input())
print(is_leap(year))
