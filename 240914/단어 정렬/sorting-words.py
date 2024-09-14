n = int(input())

s = list()

for i in range(n):
    s.append(input())

s.sort()

for word in s:
    print(word)