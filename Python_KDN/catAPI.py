import requests as re

URL = 'https://api.thecatapi.com/v1/images/search'
response = re.get(URL)
data_list =[]


def cat_API():
    if response.status_code == 200:
        result = response.json()
        image = result[0].get('url')
        print(image)


if response.status_code == 200:
    result = response.json()
    # print(result)
    # print(type(result))

    for i in range(0, len(result)):
        data_list.append(result[i]['url'])
    print(data_list)

cat_API()

    # image = result[0].get('image')
    # print(image)
    # image = result.get('image')
    # answer = result.get('answer')
    # image = result.get('image')
    # print(answer, image)

