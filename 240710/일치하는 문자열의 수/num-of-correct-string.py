n, a = input().split()
n = int(n)
cnt = 0
for _ in range(n):
    s = input()
    if(s == a):
        cnt += 1

print(cnt)