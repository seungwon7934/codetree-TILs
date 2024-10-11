c = []
area = 0

for i in range(3):

    x1, y1, x2, y2 = map(int, input().split())

    x1 += 1000
    y1 += 1000
    x2 += 1000
    y2 += 1000


    if(i < 2):  # 겹치지 않는 직사각형 A, B의 면적 계산 후 저장, 좌표 저장
        area += (x2 - x1) * (y2 - y1)
        c.append( (x1, y1, x2, y2) )
    else:
        for j in range(2):  # 빼줘야 하는 직사각형의 좌표에 대해 A, B에 대해 겹치는 좌표 경계를 계산
            overlap_x1 = max(x1, c[j][0])
            overlap_y1 = max(y1, c[j][1])   # 더 오른쪽 값 선택 (바깥쪽)
            overlap_x2 = min(x2, c[j][2])
            overlap_y2 = min(y2, c[j][3])   # 더 왼쪽 값 선택 (안쪽)

            if(overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2):
                area -= (overlap_x2 - overlap_x1) * (overlap_y2 - overlap_y1)

print(area)