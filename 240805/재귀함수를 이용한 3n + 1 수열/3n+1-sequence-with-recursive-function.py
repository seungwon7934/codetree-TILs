n = int(input())

cnt = 0

def a(n):
    if(n == 1):
        return
    global cnt
    if(n % 2 == 0):
        cnt += 1
        a(n / 2)
    else:
        cnt += 1
        a(n * 3 + 1)

a(n)

print(cnt)