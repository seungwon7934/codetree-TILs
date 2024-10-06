n = int(input())

line = [0] * 201

for _ in range(n):
    x1, x2 = map(int, input().split())
    x1 += 100
    x2 += 100

    for i in range(x1, x2):
        line[i] += 1

m = 0

for num in line:
    if(m < num):
        m = num

print(m)