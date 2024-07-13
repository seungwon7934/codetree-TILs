def year(n):
    isTrue = False
    if(n % 4 == 0):
        isTrue = True
    
    if(n % 100 == 0 and n % 400 != 0):
        isTrue = False
    return isTrue

y = int(input())

if(year(y)):
    print("true")
else:
    print("false")