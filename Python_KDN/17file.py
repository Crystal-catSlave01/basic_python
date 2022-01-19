import os

#os.mkdir() # 폴더 만들기

f = open('./test.txt', 'w', encoding='utf-8')
f.write('글 테스트')
f.close()

# with as :
with open('./test.txt', 'w', encoding='utf-8') as f:
    f.write('글 테스트2')

import csv
with open('./KDN/test.csv', 'r', encoding='utf-8') as f:
    read_data = csv.reader(f)
    for line in read_data:
        print(line)

import json
with open('./KDN/test.josn', 'r', encoding='utf-8') as f:
    read_data = json.load(f)
    print(read_data)