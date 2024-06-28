arr = list(map(float, input().split()))

total = 0

for num in arr:
    total += num

print(f"{total / len(arr):.1f}")