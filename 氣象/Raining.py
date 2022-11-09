import requests

radar_url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0058-003?Authorization=rdec-key-123-45678-011121314&format=JSON'
radar = requests.get(radar_url)
radar_json = radar.json()
radar_img = radar_json['cwbopendata']['dataset']['resource']['uri']
radat_time = radar_json['cwbopendata']['dataset']['time']['obsTime']   # 取得時間
print(radar_img)

url = 'https://notify-api.line.me/api/notify'
token = ''
headers = {
    'Authorization': 'Bearer ' + token
}
data = {
    'message':'/n'+'從雷達回波看看會不會下雨～',
    'imageThumbnail':radar_img + '?' + radat_time,    # 加上時間參數
    'imageFullsize':radar_img + '?' + radat_time      # 加上時間參數
}
data = requests.post(url, headers=headers, data=data)
