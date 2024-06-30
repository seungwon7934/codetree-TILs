num = list(map(int, input().split()))
score = [0] * 11

for n in num:
    if(n == 0):
        break
    score[n //10] += 1

for i in range(len(score) - 1, 0, -1):
    print(f"{i * 10} - {score[i]}")