def find_digits(n):
    isTrue = False
    
    while(n != 0):
        q = n // 10
        r = n % 10

        if(r != 0) and (r % 3 == 0):
            isTrue = True
            break
        n = q
    return isTrue

def three_multiple(n):
    return n % 3 == 0

a, b = map(int, input().split())
total = 0

for i in range(a, b + 1):
    if(find_digits(i) or three_multiple(i)):
        total += 1

print(total)