n = input()
m = int(n, 16)

for i in range(1,16):
    value = m * i
    print('%s*%X=%X'%(n,i,value))