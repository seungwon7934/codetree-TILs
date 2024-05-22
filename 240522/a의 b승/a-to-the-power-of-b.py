a, b = map(int, input().split())

n = 1

for i in range(1, b+1):
    n *= a

print(n)