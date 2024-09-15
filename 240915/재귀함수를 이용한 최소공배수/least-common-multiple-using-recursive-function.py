import math

n = int(input())
arr = map(int, input().split())
arr = list(arr)

def lcm(m, a):
    global n
    if(a == n):
        return m
    if(a == 0):
        m = (arr[0] * arr[1]) // math.gcd(arr[0], arr[1])
    else:
        m = (m * arr[a]) // math.gcd(m, arr[a])
    return lcm(m, a+1)

print(lcm(1, 0))