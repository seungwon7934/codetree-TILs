def is_prime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True


def sum_prime(a, b):
    total = 0
    for i in range(a, b+1):
        if(is_prime(i)):
            total += i
    return total

a, b = map(int, input().split())

if(b == 1):
    print(1)

print(sum_prime(a, b))