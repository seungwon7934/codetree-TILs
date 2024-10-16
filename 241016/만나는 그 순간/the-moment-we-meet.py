n, m = map(int, input().split())
idx = 0
time = 0
a = {}
b = {}

for _ in range(n):
    d, t = input().split()
    t = int(t)

    if(d == "R"):
        for i in range(time, time + t):
            a[i] = idx
            idx += 1
    
    else:
        for i in range(time, time + t):
            a[i] = idx
            idx -= 1

    time += t

idx = 0
time = 0
for _ in range(m):
    d, t = input().split()
    t = int(t)

    if(d == "R"):
        for i in range(time, time + t):
            b[i] = idx
            idx += 1
    
    else:
        for i in range(time, time + t):
            b[i] = idx
            idx -= 1

    time += t

t = 0
for t in range(1, len(a)):
    if(a[t] == b[t]):
        print(t)
        break
    
if(t == len(a) - 1):
    print(-1)