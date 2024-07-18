def palindrome(s):
    if(s == ''.join(reversed(s))):
        return "Yes"
    else:
        return "No"

s = input()

print(palindrome(s))