total = 0
for _ in range(2):
    s = input()
    num = ''
    for i in range(len(s)):
        if(48 <= ord(s[i]) <= 57):
            num = num + s[i]
    total += int(num)

print(total)