a = int(input())
m = list(map(int, input().split()))

for i in range(len(m)-1, -1, -1):
    print(m[i], end=' ')