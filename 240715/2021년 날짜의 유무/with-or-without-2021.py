def isTrue(m, d):
    if(m > 12):
        return False
    else:
        if(m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            if(d > 31):
                return False
            else:
                return True

        else:
            if(m == 2):
                if(d > 28):
                    return False
                else:
                    return True
            if(d > 30):
                return False
            else:
                return True


m, d = map(int, input().split())

if(isTrue(m, d)):
    print("Yes")
else:
    print("No")