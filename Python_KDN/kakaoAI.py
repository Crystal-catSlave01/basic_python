import requests

URL = 'https://dapi.kakao.com'
method = '/v2/vision/face/detect' # HTTP/1.1
REST_API_KEY = '0d697b65f56b16945652e869874c8a4d'

headers = {
    'Authorization': f'KakaoAK {REST_API_KEY}'
}

image_url = 'https://zip-sa.github.io/assets/img/me/me.jpeg'
data = { 'image_url': image_url}

response = requests.post(URL + method, headers=headers, data=data)

if response.status_code == 200:
    result = response.json()

    data = result['result']['faces'][0]['facial_attributes']
    gender = data.get('gender')
    age = data.get('age')

    if gender.get('male') > gender.get('female'):
        print("남성입니다.")
    else:
        print('여성입니다.')

    print(f'나이가 {age}로 예측됩니다.')
    print(result)