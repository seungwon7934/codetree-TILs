n, m = map(int, input().split())

result = [[0] * m for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

dir_num = 0

x, y = 0, 0

def in_range(x, y):
    return x >= 0 and x <= m and y >= 0 and y <= n

for i in range(n * m):
    result[y][x] = i + 1

    if(in_range(x + dx[dir_num], y + dy[dir_num]) == False and result[y + dy[dir_num]][x + dx[dir_num]] != 0):
        dir_num = (dir_num + 1) % 4

    x, y = x + dx[dir_num], y + dy[dir_num]

for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    print()