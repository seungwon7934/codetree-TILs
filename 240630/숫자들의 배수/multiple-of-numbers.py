n = int(input())

cnt = 0

for i in range(1, 11):
    if((i * n) % 5 == 0):
        cnt += 1
    if(cnt == 3):
        break
    print(i * n, end=' ')