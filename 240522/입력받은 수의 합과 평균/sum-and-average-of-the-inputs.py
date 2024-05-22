n = int(input())

total = 0
avg = 0

for i in range(n):
    a = int(input())
    total += a

avg = total/n

print(f"{total} {avg:.1f}")