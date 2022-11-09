from openpyxl import Workbook
import requests

wbTitle = ['站點代號', '場站中文名稱', '場站總停車格', '場站目前車輛數量', '場站區域', '資料更新時間',
           '緯度', '經度', '地點', '場站區域英文', '場站名稱英文', '地址英文', '空位數量', '全站禁用狀態']

url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
wb=Workbook()
ws=wb.create_sheet('Ubike',0)

ws.append(wbTitle)

arr=[]
if __name__ == "__main__":
    response  = requests.get(url)
    Ubike = response.json()
    UbikeNums = Ubike['retVal'].keys()
    UbikeTitles = Ubike['retVal']['0001'].keys()

    for UbikeNum in UbikeNums:
        for UbikeTitle in UbikeTitles:
            arr += [Ubike['retVal'][UbikeNum][UbikeTitle]]
        ws.append(arr)
        arr = []
wb.save('台北市Ubike即時資料.xlsx')