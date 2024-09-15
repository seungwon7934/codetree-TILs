import math

n = int(input())
arr = map(int, input().split())
arr = list(arr)

def lcm(m, a):
    global n
    if( (a + 1) == n):
        return m
    if(a == 0):
        m = (arr[a] * arr[a+1]) // math.gcd(arr[a], arr[a+1])
    else:
        m = (m * arr[a+1]) // math.gcd(m, arr[a+1])
    return lcm(m, a+1)

print(lcm(1, 0))