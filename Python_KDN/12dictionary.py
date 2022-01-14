#dict

# dict()
# {}

data ={
    '1' : 'one',
    '2' : 'two',
}

data['3'] = 'three'
del data['1']

# print(data['3'])

# 추가 = 할당
# 삭제 del

data = {'1' : 'one', '2' : 'two', (1,2) : '345'}
result = data.keys() # keys() .key값 찾기, .values() value 찾기, .items() = 튜플 형태 -> key : value
print(result)
print(type(result))
print(list(result))
# keys()
print(data)

# asdasd

for key, value in data.items():
    print(f'key:{key} / value: {value}')

# list와 dict에서 값을 찾는 것 ->  O(N) : O(1~N) = list : dict

print(data.get('3'))

check = ['1', '2', '3']

for num in check:
    if data.get(num):
        print(data[num])
    else:
        print('키값 없음')
