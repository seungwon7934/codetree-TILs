def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

n = int(input())

arr = []

for _ in range(n):
    arr.append(input().split())

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

total = 0
cnt = 0
for i in range(n):
    for j in range(n):

        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy

            if in_range(nx, ny) and arr[nx][ny] == "1":
                cnt += 1
        
        if(cnt >= 3):
            total += 1

        cnt = 0

print(total)