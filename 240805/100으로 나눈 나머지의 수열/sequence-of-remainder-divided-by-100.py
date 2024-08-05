n = int(input())

def asd(n):
    if(n == 1):
        return 2
    elif(n == 2):
        return 4
    else:
        return (asd(n-1) * asd(n-2)) % 100

print(asd(n))