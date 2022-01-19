# comprehension 컴프리헨션

"""
1. list_data = [ 변수 for 변수 in iterable_객체]
2. list_data = [ 변수 for 변수 in 객체 if 조건식]
3. list_data = [ 삼항연산자 for 변수 in iterable_객체]

4. list_data = [
5.

"""

data = [[0]*5 for _ in range(5)]
print(data, end='\n\n\n')



for line in data:
    print(line)
    
# 가독성
# 성능