s1 = list(input())
s2 = s1[:]

for i in range(len(s1)):
    if(s1[i] == s2[0]):
        s1[i] = s2[1]
    elif(s1[i] == s2[1]):
        s1[i] = s2[0]

s = ''.join(s1)
print(s)