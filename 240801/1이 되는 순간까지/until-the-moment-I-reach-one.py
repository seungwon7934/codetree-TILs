n = int(input())
cnt = 0

def s(n):
    global cnt
    if(n == 1):
        return n
    if(n % 2 == 0):
        s(n // 2)
        cnt += 1
    else:
        s(n // 3)
        cnt += 1

s(n)
print(cnt)