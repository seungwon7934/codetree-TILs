s = input()
total = 0

for c in s:
    if(48 <= ord(c) <= 57):
        total += ord(c) - 48

print(total)