n, m = map(int, input().split())
cnt = 0
time = 0
idx = 0
a = {}
b = {}

for _ in range(n):
    v, t = map(int, input().split())

    for i in range(time, time + t + 1):
        a[i] = idx
        idx += v
    time += t


time = 0
idx = 0
for _ in range(m):
    v, t = map(int, input().split())

    for i in range(time, time + t + 1):
        b[i] = idx
        idx += v
    time += t



for i in range(len(a)):
    if(i == 0):
        continue

    if(a[i-1] >= b[i-1] and a[i] < b[i]): # B가 앞지르는 경우
        cnt += 1

    if(b[i-1] >= a[i-1] and b[i] < a[i]): # A가 앞지르는 경우
        cnt += 1

print(cnt - 1)