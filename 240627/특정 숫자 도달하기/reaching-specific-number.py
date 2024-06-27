arr = list(map(int, input().split()))

total = 0
cnt = 0
for num in arr:
    if(num >= 250):
        break;
    else:
        total += num
        cnt += 1

print(f"{total} {total / cnt:.1f}")