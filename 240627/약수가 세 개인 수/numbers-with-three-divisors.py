start, end = map(int, input().split())

cnt = 0
for i in range(start, end + 1):
    f = 0
    for j in range(1, i + 1):
        if(i % j == 0):
            f += 1

    if(f == 3):
        cnt += 1

print(cnt)