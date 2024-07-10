a, b = input().split()
idx = 0
total = 0

for c in a:
    if(48 <= ord(c) <= 57):
        idx += 1
    else:
        break

total += int(a[:idx])
idx = 0

for c in b:
    if(48 <= ord(c) <= 57):
        idx += 1
    else:
        break

total += int(b[:idx])
print(total)