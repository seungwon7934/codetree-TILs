a, b = map(int, input().split())

total = 0
cnt = 0
avg = 0

for i in range(a, b+1):
    if(i % 5 == 0 or i % 7 == 0):
        total += i
        cnt += 1

avg = total/cnt

print(f"{total} {avg:.1f}")