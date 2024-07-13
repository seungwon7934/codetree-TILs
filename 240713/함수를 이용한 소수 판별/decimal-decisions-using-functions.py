def is_prime(n):
    for i in range(1, n):
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

print(sum_prime(a, b))