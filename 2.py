a, b = map(int, input().strip().split('x'))
c, d, e = map(int, input().strip().split('x'))

hole = sorted([a, b])
brick = sorted([c, d, e])

if (brick[0] <= hole[0] and brick[1] <= hole[1]) or (brick[0] <= hole[1] and brick[1] <= hole[0]):
    print("да")
else:
    print("нет")
