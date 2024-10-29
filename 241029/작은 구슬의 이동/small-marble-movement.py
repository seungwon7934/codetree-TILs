dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
dir_num = 0
n, t = map(int, input().split())
r, c, d = input().split()
r = int(r)
c = int(c)
y, x = r-1, c-1

if(d == "U"):
    dir_num = 0
elif(d == "D"):
    dir_num = 1
elif(d == "L"):
    dir_num = 2
else:
    dir_num = 3


for _ in range(t):
    x, y = x + dx[dir_num], y + dy[dir_num]

    if(x == n):
        dir_num = 2
        x -= 1
        continue
    if(x == -1):
        dir_num = 3
        x += 1
        continue
    if(y == n):
        dir_num = 1
        y -= 1
        
    if(y == -1):
        dir_num = 2
        y += 1

print(y+1, x+1)