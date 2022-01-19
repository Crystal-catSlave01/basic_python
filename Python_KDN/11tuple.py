# tuple

"""
packing
하나의 변수에 여러 개의 값을 넣는 것

Unpacking
패킹된 변수에서 여러 개의 값을 꺼내는 것
"""

a = 1, 3, 5
x, y, z =a
print(a)
print(type(a))

print(f'x: {x}, y: {y}, z: {z}')

# data = (1,2,3)
# data[2] = 5
# print(data) 에러가 남 ( 튜플은 mutable)
