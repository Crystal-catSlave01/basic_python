a = int(input())
b = int(input())
c = int(input())

r = str(a*b*c)
l = []


for i in range(0,len(r)):
    cnt = 0

    for j in range(0,10):
        if r[i] == j:
            cnt += 1
            l[j] = cnt
    print(l[j])  

print(r)