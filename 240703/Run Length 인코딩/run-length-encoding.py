s = input()
aph = s[0]
cnt = 0
enc = []
for i in range(len(s)):
    if(aph != s[i]):
        enc.append(aph)
        cnt = str(cnt)
        enc.append(cnt)
        aph = s[i]
        cnt = 0
    if(aph == s[i]):
        cnt += 1
    if(i == len(s) - 1):
        enc.append(aph)
        enc.append(cnt)

print(len(enc))

for i in range(len(enc)):
    print(enc[i],end='')