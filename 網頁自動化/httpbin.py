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

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
r = req.post(url=url, params=params, data=data, headers=headers)

print(r.text)