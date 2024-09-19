class Score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())

s = []

for _ in range(n):
    arr = input().split()
    s.append(Score(arr[0], arr[1], arr[2], arr[3]))

# s.sort(key=lambda x:(-int(x.kor), -int(x.eng), -int(x.math)))
s.sort(key=lambda x:(x.kor, x.eng, x.math))


for i in range(n-1, -1, -1):
    pp = s[i]
    print(pp.name, pp.kor, pp.eng, pp.math)