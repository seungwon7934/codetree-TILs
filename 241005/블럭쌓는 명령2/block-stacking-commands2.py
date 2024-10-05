n, k = map(int, input().split())

l = [0] * (n + 1)

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        l[i] += 1
m = 0
for i in range(len(l)):
    if (m < l[i]):
        m = l[i]

print(m)