# 3을 5번 곱한 값
print("3을 5번 곱한 값")
print(3**5)
print(3*3*3*3*3)
print("-------------------------------")

# 1.2 - 0.1
print("1.2 - 0.1 값 구하기")
a = 1.2
b = 0.1

print(a,b)
print(round(1.2 - 0.1, 2))
print("-------------------------------")

# 구구단 한 가지
print("구구단 만들기\n")
num = int(input('몇단? : '))

#for i in range(1,10):
#    print(f'{num} * {i} = {num*i}')

print("-------------------------------")
# 구구단 ALL
print('구구단 모두 출력\n')

for i in range(1,10):
    print(f'{i}단 출력')
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')
    print('\n')

print('구구단 종료\n')
print("-------------------------------")

