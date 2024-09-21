class Dot:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index

n = int(input())

d = []
idx = 1

for _ in range(n):
    x, y = map(int, input().split())
    d.append(Dot(x, y, idx))
    idx += 1


d.sort(key=lambda dot:(abs(dot.x) + abs(dot.y)))

for i in range(n):
    dd = d[i]
    print(dd.index)