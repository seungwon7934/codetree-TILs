n = int(input())

def s(n):
    if(n < 10):
        return n ** 2
    return s(n // 10) + (n % 10) ** 2

print(s(n))