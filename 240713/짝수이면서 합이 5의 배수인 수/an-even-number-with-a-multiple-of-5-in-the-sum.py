def even(n):
    return n % 2 == 0

def sum_digits(n):
    total = 0
    while(n != 0):
        q = n // 10
        r = n % 10
        total += r
        n = q
    return total % 5 == 0

n = int(input())

if(even(n) and sum_digits(n)):
    print("Yes")
else:
    print("No")