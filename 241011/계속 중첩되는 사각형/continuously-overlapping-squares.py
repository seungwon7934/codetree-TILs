c = {}
n = int(input())

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    if(i % 2 == 0):
        for x in range(x1, x2):
            for y in range(y1, y2):
                c[(x, y)] = "r"
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                c[(x, y)] = "b"

total = 0

for (x, y) in c:
    if(c.get((x, y)) == "b"):
        total += 1

print(total)