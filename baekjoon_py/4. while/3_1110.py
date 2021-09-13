n = int(input())
count = 0

def transfer(n):

    if n < 10:
        n = n*10
    a = int(n / 10)
    b = int(n % 10)
    c = int((a + b) % 10)

    return a,b,c

r = transfer(n)

while True:

    count += 1
    if r[1]+r[2] == n:
        break
    else:
        r[0] = r[1]
        r[1] = r[2]
        r[2] = r[1] + r[2]


# def transfer(n):
    
#     if n < 10:
#         n = n*10

#     a = int(n / 10)
#     b = int(n % 10)
#     c = int((a + b) % 10)

#     return a,b,c

# def calculator(result):
#     return result[1] + result[2]

# result = transfer(n)

