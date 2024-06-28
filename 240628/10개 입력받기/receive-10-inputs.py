arr = list(map(int, input().split()))

cnt = 0
total = 0

for num in arr:
    if (num == 0):
        break
    else:
        total += num
        cnt += 1

print(f"{total} {total / cnt:.1f}")