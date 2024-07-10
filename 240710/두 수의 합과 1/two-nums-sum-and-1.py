a, b = map(int, input().split())
n = a + b

cnt = 0

while(n != 0):
    r = n // 10
    q = n % 10
    if(q == 1):
        cnt += 1
    n = r

print(cnt)