# for 문
# for 변수 in iterable:
# for 변수 in range(len(iterable)):

# range
"""
1. range(end)
2. range(start, end, step)
    단, end는 끝점을 포함하지 않음
"""

numbers = range(1, 11, 1) # iterable 객체

for i in range(10):
    print(i)

print("============================")
print("============================")
print("============================")

# while 문

# continue
for i in range(10):
    if i == 5:
        continue
    print(i)
print("============================")

# break
for i in range(10):
    if i == 5:
        break
    print(i)
print("============================")

# enumerate
"""
열거하다. 인덱스 값 나열할 때
"""
for key, value in enumerate(range(10, 20)):
    print(f'key: {key} / value: {value}')
print("============================")
