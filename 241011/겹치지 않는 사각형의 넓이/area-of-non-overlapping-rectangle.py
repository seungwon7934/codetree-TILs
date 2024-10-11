c = {}

min_x = 2000
min_y = 2000

for i in range(3):

    x1, y1, x2, y2 = map(int, input().split())

    x1 += 1000
    y1 += 1000
    x2 += 1000
    y2 += 1000

    if(min_x > x1):
        min_x = x1
    
    if(min_y > y1):
        min_y = y1

    if(i < 2):
        for x in range(x1, x2):
            for y in range(y1, y2):
                c[(x,y)] = 1
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                if( (x,y) in c):
                    del c[(x, y)]

print(len(c.keys()))