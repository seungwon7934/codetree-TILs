c = {}
n = int(input())


for _ in range(n):
    x1, y1 = map(int, input().split())

    for i in range(x1, x1 + 8):
        for j in range(y1, y1 + 8):
            c[(i, j)] = 1

print(len(c.keys()))