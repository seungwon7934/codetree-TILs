total = 0
cnt = 0

while(True):
    n = int(input())
    if(n >= 30 or n <= 19):
        break
    else:
        total += n
        cnt += 1

else:
    print(f"{total/cnt:.2f}")