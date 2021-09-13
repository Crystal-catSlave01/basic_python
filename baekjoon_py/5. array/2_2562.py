l = []

for i in range(9):
    l.append(int(input()))

temp = max(l)
index = l.index(temp)

print(temp)
print(index+1)