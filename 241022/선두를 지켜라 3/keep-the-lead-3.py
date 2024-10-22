def location(arr, n):
    time = 1
    idx = 0

    for _ in range(n):
        v, t = map(int, input().split())

        for i in range(time, time + t):
            idx += v
            arr[i] = idx
        time += t

N, M = map(int, input().split())

a = {}
b = {}
h = []
cnt = 1

location(a, N)
location(b, M)

for i in range(1, len(a)):
    if(a[i] > b[i]):
        h.append("a")
    elif(a[i] < b[i]):
        h.append("b")
    else:
        h.append("c")

for i in range(1, len(h)):
    if(h[i-1] != h[i]):
        cnt += 1

print(cnt)