arr = []
cnt = 0

for _ in range(200):
    s = input()
    if(s == '0'):
        break
    else:
        arr.append(s)
        cnt += 1

print(cnt)

for i in range(0, len(arr), 2):
    print(arr[i])