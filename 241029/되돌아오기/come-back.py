x, y = 0, 0
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
t = 1
arr = {}

n = int(input())

def moving(dir_num, arr, m):
    global x, y, dx, dy, t
    for i in range(t, t + m):
        x, y = x + dx[dir_num], y + dy[dir_num]

        if(x == 0 and y == 0):
            return i

        arr[i] = (y, x)
    
    t += m
    return 0


result = 0

for i in range(n):
    d, m = input().split()
    m = int(m)
    if(d == "N"):
        idx = moving(0, arr, m)
    elif(d == "S"):
        idx = moving(1, arr, m)
    elif(d == "W"):
        idx = moving(2, arr, m)
    else:
        idx = moving(3, arr, m)

    if(idx != 0):
        result = idx

if(result == 0):
    print(-1)
else:
    print(result)