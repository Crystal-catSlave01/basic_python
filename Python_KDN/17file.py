import os

#os.mkdir() # 폴더 만들기

f = open('./test.txt', 'w', encoding='utf-8')

f.write('글 테스트')

f.close()