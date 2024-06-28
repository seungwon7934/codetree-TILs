n = int(input())
cnt = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    avg = 0
    for grade in arr:
        avg += grade
    if(avg / len(arr) >= 60):
        cnt += 1
        print("pass")
    else:
        print("fail")

print(cnt)