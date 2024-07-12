def gcd(n, m):
    num = 0
    for i in range(1, 101):
        if(n % i == 0 and m % i == 0):
            num = i
    return num

n, m = map(int, input().split())

num = gcd(n, m)
print(num)