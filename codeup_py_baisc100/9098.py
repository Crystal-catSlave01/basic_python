board=[[]*10 for _ in range(10)]
for i in range(10):
    board[i]=list(map(int,input().split()))
x=1
y=1
board[x][y]=9

while True:
    if(board[x][y]==2):
        board[x][y]=9
        break
    if(board[x][y+1]!=1):
        board[x][y]=9
        y+=1
    else:
        if(board[x+1][y]!=1):
            board[x][y]=9
            x+=1
        else:
          board[x][y]=9
          break

for i in range(10):
    for j in range(10):
        print(board[i][j],end=' ')
    print()
    #복습