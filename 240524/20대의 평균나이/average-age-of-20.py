total = 0
cnt = 0

while(True):
    n = int(input())
    if(n >= 30):
        break
    total += n
    cnt += 1

print(f"{total/cnt:.2f}")