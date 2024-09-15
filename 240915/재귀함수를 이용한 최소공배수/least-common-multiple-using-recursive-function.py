import math

def lcm(m, a):
    global n
    if(a == n):
        return m
    if(a == 0):
        m = (arr[0] * arr[1]) // math.gcd(arr[0], arr[1])
    else:
        m = (m * arr[a]) // math.gcd(m, arr[a])
    return lcm(m, a+1)

n = int(input())
arr = map(int, input().split())
arr = list(arr)

if(len(arr) == 1):
    print(arr[0])
else:
    print(lcm(1, 0))