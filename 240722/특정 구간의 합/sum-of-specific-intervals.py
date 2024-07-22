n, m = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(m):
    total = 0
    a1, a2 = map(int, input().split())
    for i in range(a1 - 1, a2):
        total += a[i]
    print(total)