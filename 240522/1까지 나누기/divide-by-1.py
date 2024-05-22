n = int(input())

i = 0
while(n >= 1):
    i += 1
    n /= i
    if(n <= 1):
        break;

print(i)