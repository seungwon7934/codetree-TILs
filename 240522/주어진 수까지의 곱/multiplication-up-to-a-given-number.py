m = 1

a, b = map(int, input().split())

for i in range(a, b+1):
    m *= i

print(m)