import pandas as pd
from pandas import ExcelWriter

url = 'https://quality.data.gov.tw/dq_download_csv.php?nid=25489&md5_url=a85eb04185242dd82bf3db71756eb6da'
dfOpenData = pd.read_csv(url, encoding='utf-8')
print(dfOpenData[['行政區名', '中心點經度', '中心點緯度']])

df = pd.read_excel('1111人力銀行.xlsx', '1111人力銀行')

print(df.head())

#dfOpenData['地點'] = df['工作地點']
a=dfOpenData['行政區名']
print(type(a))
for i in df['工作地點']:
    if i in dfOpenData['行政區名']:
        print(i)


if df[df['工作地點'] == dfOpenData['行政區名']]:
    df['經度'] = dfOpenData['中心點經度']
    df['緯度'] = dfOpenData['中心點緯度']



print(df.head())


writer = ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet1')
writer.save()
