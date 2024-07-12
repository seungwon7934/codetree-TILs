def lcm(n, m):
    num = 0
    for i in range(1, n*m + 1):
        if(i % n == 0 and i % m == 0):
            num = i
            break
    return num

n, m = map(int, input().split())
print(lcm(n, m))