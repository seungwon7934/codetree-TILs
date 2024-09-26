month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


m1, d1, m2, d2 = map(int, input().split())

m = m2 - m1
d = 0

if(m == 0):
    d = d2 - d1
elif(m > 0):
    for i in range(m1, m1 + m):
        d += month_day[i]
    d = d - d1 + d2
else:
    for i in range(m2, m1 - m):
        d += month_day[i]
    d = d + d1 - d2


print(days[(7 - (7-d) % 7) % 7])

# 1. 처음 날짜랑 두 번째 날짜를 비교함
# 2. 두 가지 경우로 나뉨
#     1) 두 번째 날짜가 나중인 경우
#     2) 두 번째 날짜가 이전인 경우

# 3. 1) 일 때는 단순하게 계산해서 시작 달로부터 차이나는 달 개수 * [days] - 처음 날짜 + 나중 날짜
#    2) 일 때는 이전 달의 개수 * [days] - 처음 날짜 + 나중 날짜 

# ex1) 5/3 - 6/1
#      달: 1
#      31 - 3 + 1 = 29

# ex2) 6/1 - 5/3
#      달: -1
#      31 + 1 - 3 = 29