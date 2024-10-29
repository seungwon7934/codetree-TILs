x, y = 0, 0
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
t = 1
arr = {}

n = int(input())

def moving(dir_num, arr, m):
    global x, y, dx, dy, t
    for i in range(t, t + m):
        x, y = x + dx[dir_num], y + dy[dir_num]
        arr[i] = (y, x)
    
    t += m


result = 0

for i in range(n):
    d, m = input().split()
    m = int(m)
    if(d == "N"):
        moving(0, arr, m)
    elif(d == "S"):
        moving(1, arr, m)
    elif(d == "W"):
        moving(2, arr, m)
    else:
        moving(3, arr, m)

for i in arr:
    if(arr[i] == (0, 0)):
        print(i)
        break
    if(i == len(arr) - 1 and arr[i] != (0, 0)):
        print(-1)