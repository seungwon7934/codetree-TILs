def s(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    return n + s(n-2)

n = int(input())

print(s(n))