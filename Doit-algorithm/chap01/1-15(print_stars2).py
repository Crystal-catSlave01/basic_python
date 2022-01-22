# *를 n개 출력하되 w마다 줄바꿈 하기 2

print('It will be printed star')
n = int(input('How many stars do you want to print? : '))
w = int(input('How many stars should I change the line? : '))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)