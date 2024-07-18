def isLeap(y):
    if(y % 4 == 0 and y % 100 == 0 and y % 400 == 0):
        return True
    if(y % 4 == 0 and y % 100 == 0):
        return False
    if(y % 4 == 0):
        return True
    return False

def isPresent(leap, m, d):
    if(leap == True and m == 2 and d > 29):
        return -1
    if(m == 1 or 3 or 5 or 7 or 8 or 10 or 12):
        if(d > 31):
            return -1
        else:
            return m
    elif(m == 4 or 6 or 9 or 11):
        if(d > 30):
            return -1
        else:
            return m
    else:
        if(d > 28):
            return -1
        else:
            return m



y, m, d = map(int, input().split())

leap = False
season = 999
present = False

season = isPresent(isLeap(y), m, d)

if(3 <= season <= 5):
    print("Spring")
elif(6 <= season <= 8):
    print("Summer")
elif(9 <= season <= 11):
    print("Fall")
elif(1 <= season <= 2 or season == 12):
    print("Winter")
else:
    print(-1)