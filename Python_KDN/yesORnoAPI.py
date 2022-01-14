import requests as re

URL = 'https://yesno.wtf/api'

response = re.get(URL)

if response.status_code == 200:
    result = response.json()
    print(type(result))
    answer = result.get('answer')
    image = result.get('image')
    print(answer, image)