n = int(input())
count = 0

if n < 10:
    n = n*10

def transfer(n):

    a = int(n / 10)
    b = int(n % 10)
    c = int((a + b) % 10)

    return a,b,c

r0 = transfer(n)
r = [r0[0],r0[1],r0[2]]
a,b,c = r

if n / 10 == 0:
    a = r[0]
    b = r[0]
    c = (a+b)%10
    count += 1

while True:

    count += 1

    a = r[0]
    b = r[1]
    c = r[2]

    r[0] = b
    r[1] = c
    r[2] = int((b + c) % 10)

    if b*10 + c == n:
        break

if n == 0:
    count = 1

print(count)