# c = {}
# x_min = y_min = x_max = y_max = 0
# x1, y1, x2, y2 = map(int, input().split())
# x3, y3, x4, y4 = map(int, input().split())

# x1 += 1000
# x2 += 1000
# x3 += 1000
# x4 += 1000

# y1 += 1000
# y2 += 1000
# y3 += 1000
# y4 += 1000

# for x in range(x1, x2):
#     for y in range(y1, y2):
#         c[(x, y)] = 1

# for x in range(x3, x4):
#     for y in range(y3, y4):
#         if((x, y) in c):
#             del c[(x, y)]

# keys_list = list(c.keys())

# if (len(keys_list)  == 0):
#     print(0)

# else:
#     # 남아있는 좌표의 최소 및 최대 경계 찾기
#     x_min = min(key[0] for key in keys_list)
#     y_min = min(key[1] for key in keys_list)
#     x_max = max(key[0] for key in keys_list)
#     y_max = max(key[1] for key in keys_list)

#     print( (x_max - x_min + 1) * (y_max - y_min + 1))

c = {}
x_min = y_min = float('inf')
x_max = y_max = float('-inf')

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

x1 += 1000
x2 += 1000
x3 += 1000
x4 += 1000
y1 += 1000
y2 += 1000
y3 += 1000
y4 += 1000

# 첫 번째 사각형 저장하면서 최소 및 최대 경계 추적
for x in range(x1, x2):
    for y in range(y1, y2):
        c[(x, y)] = 1
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x)
        y_max = max(y_max, y)

# 두 번째 사각형과 겹치는 좌표 제거
for x in range(x3, x4):
    for y in range(y3, y4):
        if (x, y) in c:
            del c[(x, y)]

# 남아있는 좌표가 있는지 확인
if len(c) == 0:
    print(0)
else:
    # 남아있는 좌표의 경계값 확인
    x_min = min(key[0] for key in c)
    y_min = min(key[1] for key in c)
    x_max = max(key[0] for key in c)
    y_max = max(key[1] for key in c)
    
    # 최소 면적의 사각형 계산
    min_area = (x_max - x_min + 1) * (y_max - y_min + 1)
    print(min_area)