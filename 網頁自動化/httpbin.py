import requests as req

url = f'https://httpbin.org/post'

params = {
    'page': '2',
    'count': '5'
}

data = {
    'name': 'Dennis',
    'age': '26'
}
r = req.post(url, params=params, data=data)

print(r.text)