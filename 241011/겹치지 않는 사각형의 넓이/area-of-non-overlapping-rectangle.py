c = {}

for i in range(3):

    x1, y1, x2, y2 = map(int, input().split())

    x1 += 1000
    y1 += 1000
    x2 += 1000
    y2 += 1000

    if(i < 2):
        for x in range(x1, x2):
            for y in range(y1, y2):
                c[(x,y)] = 1
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                c[(x,y)] = 0

total = 0

for x in range(2000):
    for y in range(2000):
        if(c.get( (x,y) )):
            total += 1

print(total)