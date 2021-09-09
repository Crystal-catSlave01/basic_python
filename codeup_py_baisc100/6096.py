a = [[]*19 for _ in range(19)]
for i in range(19):
   a[i]=list(map(int,input().split()))

n = int(input())

for i in range(n):
    b,c=map(int,input().split())
    
    for j in range(19):
        if(a[b-1][j]==1):
            a[b-1][j]=0
        else: a[b-1][j]=1
    
    for j in range(19):
        if(a[j][c-1]==1):
            a[j][c-1]=0
        else: a[j][c-1]=1

for i in range(19):
    for j in range(19):
        print(a[i][j],end=' ')
    print()

    #복습