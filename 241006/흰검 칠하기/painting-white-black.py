class Tile:
    def __init__(self, index=0, color='none', count=0):
        self.index = index
        self.color = color
        self.count = count


n = int(input())
idx = 1000000
line = []
for _ in range(n):
    x, d = input().split()
    x = int(x)

    if(d == "L"):
        if(len(line) == 0):
            for i in range(idx, idx - x, -1):
                line.append(Tile(i, "w", 1))

        else:
            for i in range(idx, idx - x, -1):
                exist = False

                for tile in line:
                    if(tile.index == i):
                        tile.color += "w"
                        tile.count += 1
                        exist = True
                        break;

                if(exist == False):
                    line.append(Tile(i, "w", 1))
        idx -= x - 1

    else:
        if(len(line) == 0):
            for i in range(idx, idx + x):
                line.append(Tile(i, "b", 1))

        else:
            for i in range(idx, idx + x):
                exist = False

                for tile in line:
                    if(tile.index == i):
                        tile.color += "b"
                        tile.count += 1
                        exist = True
                        break;
                        
                if(exist == False):
                    line.append(Tile(i, "b", 1))
        idx += x - 1

w = b = g = 0

# for tile in line:
#     print(tile.index, tile.color, tile.count)

# for tile in line:
#     arr = list(tile.color)

#     count_w = 0
#     count_b = 0

#     for c in arr:
#         if(c == "w"):
#             count_w += 1
#         else:
#             count_b += 1

#     if(count_w >= 2 and count_b >= 2):
#         g += 1

#     else:
#         if(arr[len(arr) - 1] == "w"):
#             w += 1
#         else:
#             b += 1

# print(w, b, g)

for tile in line:
    arr = list(tile.color)

    if(len(arr) < 4):
        if(arr[len(arr)-1] == "w"):
            w += 1
        else:
            b += 1
    else:
        count_w = 0
        count_b = 0

        for c in arr:
            if(c == "w"):
                count_w += 1
            else:
                count_b += 1

        if(count_w >= 2 and count_b >= 2):
            g += 1

        else:
            if(arr[len(arr) - 1] == "w"):
                w += 1
            else:
                b += 1

print(w, b, g)