a = int(input())
b = int(input())
c = int(input())

r = list(str(a * b * c))

for i in range(10):
    print(r.count(str(i)))