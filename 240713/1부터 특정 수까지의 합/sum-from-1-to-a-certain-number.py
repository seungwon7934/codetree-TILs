def add(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total // 10


n = int(input())
print(add(n))