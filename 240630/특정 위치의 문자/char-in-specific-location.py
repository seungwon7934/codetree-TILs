word = ['L', 'E', 'B', 'R', 'O', 'S']

c = input()

for i, char in enumerate(word):
    if char == c:
        print(i)
        break
        
    if(i == len(word) - 1):
        print("None")