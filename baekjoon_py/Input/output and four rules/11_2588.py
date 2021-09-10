a = int(input()) 
b = input()
r = []

for i in range(len(b)-1, -1, -1):
    for j in range(1, len(b),):
        r[j] = int(b[i])*a*j