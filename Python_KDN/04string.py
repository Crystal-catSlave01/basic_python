#문자열 타입 (+랑 * 연산만 가능)

myString = ['문자열', 'python', '\'', 's', 'easy!']
print(myString)
print("""문자열 python's easy!""")

# ''문자열 python's easy!

data = 'Python'

print(len(data))

print(data[len(data)-1])

print(data[-1])

# 시작점 : 끝점 : 증감정도 (끝점은 포함 X)
print(data[1:4:2])
print(data[-1:-4:-1])
