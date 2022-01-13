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