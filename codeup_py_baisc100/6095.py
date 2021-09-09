board = [[0 for j in range(20)] for i in range(20)]

white = int(input())

for i in range(white):
    x, y = map(int,(input().split()))
    board[int(x)][int(y)] = 1

for i in range(1,20):
    for j in range(1,20):
        print(board[i][j], end=' ')
    print()