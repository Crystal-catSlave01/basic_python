# This code is not mine. It's a code only for practice.

import requests
import urllib
import os
from bs4 import BeautifulSoup as bs
import sys

class MaruMaru:
    def __init__(self, toon_num = 19956): # 귀멸의 칼날 19956
        self.toon_num = str(toon_num)
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
    
    def toon_url(self):
        url = 'https://marumaru.cloud/bbs/cmoic/{}'.format(self.toon_num)
        response = requests.get(url)
        html = response.content
        soup = bs(html ,'html.parser')
        info = soup.find_all('td', attrs = {'list-subject'})
        href = [info_.select('a')[0].get('href') for info_ in info]
        title = [info_.select('a')[0].get_text() for info_ in info]
        return title, href

    def img_url_lst(self, value = 3307):
        url = 'https://marumaru.cloud/bbs/cmoic/{}/{}'.format(self.toon_num, str(value))
        response = requests.get(url)
        html = response.content
        soup = bs(html, 'html.parser')
        infos = soup.find_all('img', attrs = {'img-tag'})
        url_lst = []
        for info in infos:
          info = info.get('src')
          if 'https://marumaru.cloud' not in info:
            src = 'https://marumaru.cloud' + info
          else:
            src = info
          url_lst.append(src)
        return url_lst
      
    def main(self, folder_name = 'Toon'):
      # 이미지를 저장할 폴더 만들기
        os.mkdir('./{}'.format(folder_name))      
        
        # 만화가 있는 페이지의 URL 모으기
        print('URL 모으는중')
        titles, hrefs = self.toon_url()      
        print(f'{len(titles)} 개의 화를 다운 받기 시작')

        # 다운로드 시작
        for i, (title, href) in enumerate(zip(titles,hrefs)): 
            title = title.replace('\n', '').replace('\t','').replace('\r', '')
            save_path = './{}/{}'.format(folder_name, str(len(titles)+1-i)+'.'+title)
            os.mkdir(save_path)
            # 이미지 URL 모으기
            img_urls = self.img_url_lst(value = href.split('/')[-1])
            # 이미지 다운로드         
            try:
                for j, img_url in enumerate(img_urls):
                    urllib.request.urlretrieve(img_url, '{}/{}.jpg'.format(save_path, str(j+1)))
                print(f'{title} 다운 완료')    
            except:
                print(f'{title} 다운 실패') 
                continue 

# 위에서 만든 Class 실행 
DemonSlayer = MaruMaru()
DemonSlayer.main()