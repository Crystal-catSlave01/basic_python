# *를 n개 출력하되 w개마다 줄바꿈하기 1

print('It will be printed star')
n = int(input('How many stars do you want to print? : '))
w = int(input('How many stars should I change the line? : '))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()