# 세 정수의 최댓값 구하기 함수

def max3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    print(f'max33({a},{b},{c}) = {maximum}')

max3(3,2,1)
max3(3,2,2)
max3(3,1,2)
max3(3,2,3)
max3(2,1,3)
max3(3,3,2)
max3(3,3,3)
max3(2,2,3)
max3(2,3,1)
max3(2,3,2)
max3(1,3,2)
max3(2,3,3)
max3(1,2,3)