s = input()
aph = s[0]
cnt = 0
enc = []
for i in range(len(s)):

    if(aph == s[i]):
        cnt += 1

    if(aph != s[i] or i == len(s) - 1):
        enc.append(aph)

        if(cnt >= 10):
            digit = []
            while(cnt >= 10):
                digit.append(cnt % 10)
                cnt //= 10
            digit.append(cnt)

            for j in range(len(digit) - 1, -1, -1):
                enc += str(digit[j])

        else:
            enc.append(cnt)
        
        aph = s[i]
        cnt = 1

    # if(i == len(s) - 1):
    #     enc.append(aph)
    #     enc.append(cnt)

print(len(enc))

for i in range(len(enc)):
    print(enc[i],end='')