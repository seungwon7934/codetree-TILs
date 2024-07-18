def dup(s):
    for i in range(len(s)):
        for j in range(i+1, len(s) - 1):
            if(s[i] != s[j]):
                return "Yes"
    return "Np"

s = input()
print(dup(s))