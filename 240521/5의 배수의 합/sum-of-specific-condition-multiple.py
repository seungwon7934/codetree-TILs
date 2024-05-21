a, b = map(int, input().split())

total = 0

for i in range(a, b+1):
    if(i % 5 == 0):
        total += i

print(total)