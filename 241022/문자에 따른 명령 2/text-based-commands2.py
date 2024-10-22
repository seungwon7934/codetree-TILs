dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0
dir_num = 3

N = input()

for d in N:
    if(d == "L"):
        dir_num = (dir_num - 1 + 4) % 4
    
    elif(d == "R"):
        dir_num = (dir_num + 1 + 4) % 4
    
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)