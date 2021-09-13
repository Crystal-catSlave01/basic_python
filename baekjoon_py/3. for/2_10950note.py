testcase = int(input())
a = []
b = []

for i in range(0, testcase):
    a,b.append(map(int, input().split()))

for i in range(0, testcase-1):
    print(a[i]+b[i])

