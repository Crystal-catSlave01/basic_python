print("안녕하세요. 박승우입니다.")

import keyword

#예약어 보는 방법
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

#함수 까먹었을 때 보는 거
print(dir(keyword))
"""
['__all__', '__builtins__', '__cached__', 
'__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__spec__', 'iskeyword', 'kwlist']
"""

