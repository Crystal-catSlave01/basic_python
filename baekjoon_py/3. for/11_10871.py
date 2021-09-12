n, x = map(int,input().split())
a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] < x:
        print(a[i], end=' ')
    else:
        pass