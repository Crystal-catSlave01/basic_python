# set 집합

# set()
# {}

"""
1. 중복 불가
2. 순서 x -> 인덱싱 x
3. 수정 가능(mutable) 객체
    (단, 집합 내부 원소는 불가)
"""


person = ['A', 'B', 'A', 'A', 'AB', 'O', 'AB', 'B', 'A', 'AB']

print(len(set(person)))
print(set(person))

# 집합 연산
setA = {1,2,3}
setB = {3,4,5}

print(setA | setB) # 합집합
print(setA - setB) # 차집합
print(setA & setB) # 교집합
print(setA | setB) # 대칭 = 합칩합 - 교집합