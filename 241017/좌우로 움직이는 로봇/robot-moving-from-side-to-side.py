def moving(cnt, arr):
    idx = 0
    time = 0
    for _ in range(cnt):
        t, d = input().split()
        t = int(t)

        if(d == "R"):
            for i in range(time, time + t):
                idx += 1
                arr[i] = idx
        else:
            for i in range(time, time + t):
                idx -= 1
                arr[i] = idx
        time += t


n, m = map(int, input().split())
a = {}
b = {}
l = 0
t = 0
cnt = 0
moving(n, a)
len_a = len(a)

moving(m, b)
len_b = len(b)

if(len_a >= len_b): # b가 더 짧을 때
    t = len_b
    for i in range(1, t):
        if(a[i-1] != b[i-1] and a[i] == b[i]):
            cnt += 1
    
    for i in range(t, len_a):
        if(b[t-1] == a[i]):
            cnt += 1
else:   # a가 더 짧을 때
    t = len_a
    for i in range(1, t):
        if(a[i-1] != b[i-1] and a[i] == b[i]):
            cnt += 1
    
    for i in range(t, len_b):
        if(a[t-1] == b[i]):
            cnt += 1


print(cnt)