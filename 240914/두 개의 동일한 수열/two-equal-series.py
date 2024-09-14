n = int(input())

a = list()
b = list()


nums = map(int,input().split())
for num in nums:
    a.append(num)

nums = map(int,input().split())
for num in nums:
    b.append(num)

a.sort()
b.sort()

i = 0

for i in range(len(a)):
    if(a[i] != b[i]):
        print("No")
        break

if(i == len(a) - 1):
    print("Yes")