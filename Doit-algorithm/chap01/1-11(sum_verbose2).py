# a부터 b까지 정수의 합 구하기 2

print('a부터 b가지 정수의 합을 구합니다.')
a = int(input('a : '))
b = int(input('b : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)