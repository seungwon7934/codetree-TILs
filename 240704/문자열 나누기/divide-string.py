n = int(input())



s1 = input().split()
s2 = ''

for i in range(n):
    s2 += s1[i]

for i in range(len(s2)):
    print(s2[i],end='')
    if((i + 1) % 5 == 0):
        print()