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


# 2번 다른 풀이
list_data = ['최웅', 77, '국연수', 93, '김지웅', 91, '엔제이', 88, '이솔이', 75]
name_list = list_data[0::2]
score_list = list_data[1::2]

idx = 0
maxVal = score_list[0]

for score in range(1, len(score_list)):
    if score_list[score] > maxVal:
        maxVal = score_list
        idx = score


# print((list_data))

# 3. 이중 리스트를 통하여 달팽이 그리기

data = []
imp = []
for i in range(1, 26):
    imp.append(i)
    if i % 5 == 0:
        data.append(imp)
        imp = []
print(data)

# 3.2 리스트 컴프리헨션
count = 1
graph = [[0] * 5 for _ in range(5)]
for i in range(0,5):
    for j in range(0,5):
        graph[i][j] = count
        count += 1
print(graph)

"""