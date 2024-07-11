a = input()
b = input()
cnt = -1
for i in range(len(a)):
    a = a[-1] + a[:-1]
    if(a == b):
        cnt = i + 1
        break

print(cnt)