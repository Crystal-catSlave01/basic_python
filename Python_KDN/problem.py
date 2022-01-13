"""
# 3을 5번 곱한 값
print("3을 5번 곱한 값")
print(3**5)
print(3*3*3*3*3)
print("-------------------------------")

# 1.2 - 0.1
print("1.2 - 0.1 값 구하기")
a = 1.2
b = 0.1

print(a, b)
print(round(1.2 - 0.1, 2))
print("-------------------------------")

# 구구단 한 가지
print("구구단 만들기\n")
num = int(input('몇단? : '))

for i in range(1,10):
    print(f'{num} * {i} = {num*i}')

print("-------------------------------")
# 구구단 ALL
print('구구단 모두 출력\n')

for i in range(2,10):
    print(f'{i}단 출력')
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')
    print('\n')

print('구구단 종료\n')
print("-------------------------------")


# 베스킨31 게임
print('베스킨31 게임')

for i in range (1, 32):
    if i % 10 == 3:
        print('박수')
    elif i % 10 == 6:
        print('박수')
    elif i % 10 == 9:
        print('박수')
    elif i // 10 == 3:
        print('박수')

    else:
        print(i)
"""

# 1. person  혈액형 몇명인지
print('혈액형이 몇명인지 구하시오.')
person = ['A', 'B', 'A', 'A', 'AB', 'O', 'AB', 'B', 'A', 'AB']

person.sort()
print(person)
A = person.count('A')
B = person.count('B')
AB = person.count('AB')
O = person.count('O')

print(f'A: {A} , B: {B}, AB: {AB}, O: {O}')

#for i in range(len(person)):
#    print(i)


# 2. 가장 잘 나온 학생이 몇점
print('가장 높은 점수의 학점을 구하세요.')
list_data = ['최웅', 77, '국연수', 93, '김지웅', 91, '엔제이', 88, '이솔이', 75]
list_man = []
list_point = []

for i in range(0, len(list_data)):

    if i % 2 == 1:
        list_point.append(list_data[i])
    else:
        list_man.append(list_data[i])

print(list_man)
print(list_point)

top_point = max(list_point)
top_man = list_point.index(top_point)

print(list_man[top_man])
print(top_point)

# print((list_data))

# 이중 리스트를 통하여

borad = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

spiral_list = [[0] * n for _ in range(n)]

# limit point
left = 0
right = n - 1
up = 1  # i == 0 부터 순회 하므로 up의 초기 값은 1이 된다.
down = n - 1

# 0: right, 1:down, 2:left, 3:up
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
direction = 0   # initialize to right

count = 1
i = 0
j = 0

while count <= n * n:
    spiral_list[i][j] = count
    count += 1
    # 진행방향의 끝에 도달하면 방향 전환
    if direction % 4 == 0 and j == right:
        direction += 1
        right -= 1
    elif direction % 4 == 1 and i == down:
        direction += 1
        down -= 1
    elif direction % 4 == 2 and j == left:
        direction += 1
        left += 1
    elif direction % 4 == 3 and i == up:
        direction += 1
        up += 1
    # 다음 방문할 리스트 인덱스 설정
    i += di[direction % 4]
    j += dj[direction % 4]

for e in spiral_list:
    print(e)

# borad = [],[]
#
# for i in range(5):
#     for j in range(5):
#         borad = borad.append(i,j)
#
# print(borad)
