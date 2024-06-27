n = int(input())

cnt = 1

for i in range(n):
    for j in range(n):
        if(i <= j):
            print(f"{(cnt - 1) % 9 + 1} ",end='')
            cnt += 1
        else:
            print("  ",end='')
    print()