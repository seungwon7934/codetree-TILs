n = int(input())
arr = list(map(float, input().split()))
total = 0

for num in arr:
    total += num

print(f"{total / n:.1f}")

if(total / n >= 4.0):
    print("Perfect")
elif(total / n >= 3.0):
    print("Good")
else:
    print("Poor")