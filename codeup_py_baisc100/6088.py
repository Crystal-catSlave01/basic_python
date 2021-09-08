a, d, n = map(int, input().split())
s = a

for i in range(a, n):
    s = a+(d*i)
    
print(s)