a, m, d, n = map(int, input().split())

s = a

for i in range(1, n):
    s = s*m+d
print(s)