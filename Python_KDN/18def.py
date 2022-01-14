# def 함수

def f(num):
    print(num)

f(1)

fa = lambda x, y = 3: print(x**y)
fa(3)

(lambda x, y = 3: print(x**y)) (5)