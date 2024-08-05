n = int(input())

def asd(n):
    if(n == 1):
        return 1
    elif(n == 2):
        return 2
    else:
        return asd(n//3) + asd(n-1)

print(asd(n))