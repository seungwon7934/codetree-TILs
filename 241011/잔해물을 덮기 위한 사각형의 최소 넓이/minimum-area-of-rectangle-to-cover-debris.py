# x1, y1, x2, y2 = map(int, input().split())
# x3, y3, x4, y4 = map(int, input().split())
# d1 = d2 = d3 = d4 = ()

# x1 += 1000
# x2 += 1000
# x3 += 1000
# x4 += 1000

# y1 += 1000
# y2 += 1000
# y3 += 1000
# y4 += 1000

# overlap_x1 = max(x1, x3)
# overlap_y1 = max(y1, y3)
# overlap_x2 = min(x2, x4)
# overlap_y2 = min(x2, x4)

# if(overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2):
#     d1 = (overlap_x1 - x1)

# print(n_x1, n_y1, n_x2, n_y2)


c = {}
x_min = y_min = x_max = y_max = 0
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

for x in range(x1, x2):
    for y in range(y1, y2):
        c[(x, y)] = 1

for x in range(x3, x4):
    for y in range(y3, y4):
        if((x, y) in c):
            del c[(x, y)]

keys_list = list(c.keys())

if (len(keys_list)  == 0):
    print(0)

else:
    # 남아있는 좌표의 최소 및 최대 경계 찾기
    x_min = min(key[0] for key in keys_list)
    y_min = min(key[1] for key in keys_list)
    x_max = max(key[0] for key in keys_list)
    y_max = max(key[1] for key in keys_list)

    print( (x_max - x_min + 1) * (y_max - y_min + 1))