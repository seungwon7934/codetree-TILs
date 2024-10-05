def change(n, num):
    l = []
    while(n != 0):
        l.append(n % num)
        n //= num
    l.reverse()
    return l

a, b = map(int, input().split())
n = int(input())
l = []
total = 0

l = change(n, 10)
# print(l)



# while(n != 0):
#     l.append(n % 10)
#     n //= 10
# l.reverse()

for m in l:
    total = a * total + int(m)

l.clear()

l = change(total, b)

# while(total != 0):
#     l.append(total % b)
#     total //= b
# l.reverse()

for m in l:
    print(m,end='')