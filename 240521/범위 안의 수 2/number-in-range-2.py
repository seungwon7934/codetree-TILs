total = 0
cnt = 0
avg = 0

for i in range(10):
    n = int(input())
    if(0 <= n <= 200):
        total += n
        cnt += 1

avg = total / cnt

print(f"{total} {avg:.1f}")