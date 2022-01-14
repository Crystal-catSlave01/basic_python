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

data = {'1' : 'one', 2 : 'two', (1,2) : '345'}
result = data.keys() # keys() .key값 찾기, .values() value 찾기, .items() = 튜플 형태 -> key : value
print(result)
print(type(result))
print(list(result))
# keys()
print(data)