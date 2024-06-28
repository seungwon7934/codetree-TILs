arr = list(map(int, input().split()))
total = 0
cnt = 0

for num in arr:
    if(num != 0 and num % 2 == 0):
        total += num
        cnt += 1
    elif(num % 2 != 0):
        continue
    else:
        break

print(cnt, total)