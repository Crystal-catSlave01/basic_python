# +와 -를 번갈아 출력하기 2

print('+와 -를 번갈아 출력합니다.')
n = int(input('출력 개수 : '))

for _ in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')

print()