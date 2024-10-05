month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
m1, d1, m2, d2 = map(int, input().split())
a = input()

d = 0

for i in range(m1, m2):
    d += month_day[i]

d = d - d1 + d2

q = d // 7
r = d % 7

idx = day.index(a)
# print(idx)

if(r >= idx):
    print(q + 1)
else:
    print(q)

# 1  2  3  4  5  6  7
# 화 수 목 금 토 일 월