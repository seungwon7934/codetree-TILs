a, b = map(int, input().split())

n = [0] * 10
total = 0

while(a > 1):
    n[a % b] += 1
    a = a // b

for num in n:
    total += num ** 2

print(total)