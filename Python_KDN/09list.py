#List

#mutable
val1 = [1,2,3]
val1[0] = 'p'
print(val1)

#emutable
val = 'hello'
# val[0] = 'p'
print(val)

#remove
value = [1, 2, 3, 2]
value.remove(3)
print(value)

#pop
value = [1, 2, 3, 4, 5]
result = value.pop() # -1
print(result)
print(value)

#append
value = [1, 2, 3, 4, 5]
value.append(6)
print(value)

#insert
value = [1, 2, 3, 4, 5]
value.insert(0, -1)
print(value)

#sort
value1 = [3, 2, 1]
value2 = [3, 1, 2]

result1 = value1.sort() # 반환이 없는 메서드 (클래스 안에 있으면 메서드)
result2 = sorted(value2) # 내장 함수

print(value1, result1)
print(value2, result2)
print(sorted(value2))

# sorted(val , reverse= True or False

# 메서드 / 내장함수
# 반환X  / 반환 O

# reverse
value = [3,1,2]
value.reverse()
print(value)

#index -> 인덱스 값 반환

#extend -> List객체A.extend(list객체B)

val = [3,1,2,3]
idx = val.index(3)
print(idx)