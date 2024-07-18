def dup(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if(s[i] != s[j]):
                return "Yes"
    return "No"

s = input()
print(dup(s))