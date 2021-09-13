n = int(input())
count = 0

if n < 10:
    n = n*10
    print(n)

def transfer(n):

    a = int(n / 10)
    b = int(n % 10)
    c = int((a + b) % 10)

    return a,b,c

r0 = transfer(n)
r = [r0[0],r0[1],r0[2]]
a,b,c = r
print(a,b,c)
print(type(r0[0]))

print(n%10)

while True: #r[1]*10 + r[2] != n:

    count += 1

    print(r)
    a = r[0]
    b = r[1]
    c = r[2]

    if n / 10 == 0:
        a = r[0] #9
        b = r[0] #9
        c = (a+b)%10 #8
        count += 1

    r[0] = b # 9
    r[1] = c # 8
    r[2] = int((b + c) % 10) #7



    if b*10 + c == n:
        print(count)
        break