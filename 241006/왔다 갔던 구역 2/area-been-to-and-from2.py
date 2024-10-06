n = int(input())
line = [0] * 2001
idx = 1000

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if(d == "L"):
        for i in range(idx, idx - x, -1):
            line[i] += 1
        idx = idx - x
    else:
        for i in range(idx, idx + x):
            line[i] += 1
        idx = idx + x
    

s = 0
for num in line:
    if(num >= 2):
        s += 1

print(s)