import requests
import jieba
import operator
from openpyxl import Workbook

wb=Workbook()
ws=wb.create_sheet('臉書關鍵字',0)

url = "https://graph.facebook.com/v15.0/me/posts?access_token="
token = "EAAP1quLZAFo4BABx3ZBCfckGZBVtAwbGqt1sF6DM5QdoZA7YjAtghmUL9gjakoVZBecDZBQjKHZA4F0ZAXZCi6JzOLkRzoKS9vUqSReKJXCDaL2ZBY9sZCfwszB6Lcj0JmtZBb42t6hHyvwJYX7b3gNbvD536oRrJ9SO1h3csM0n9OAV7ZAeqpWOE9auJfCGZA5E9GcZB0aHCmsesKSP74AuKcBuieeNXCnTJ8I51ckndPtQrgAyMBgiDcSlIjL"

res = requests.get(url=url+token) #得到Facebook資料
jd = res.json()   #將資料轉成json

corpus=[]
arr=[]
dic={}
if __name__ == "__main__":
    if res.status_code == requests.codes.ok:  #如果成功的話
        while 'paging' in jd:       #當還有下一頁的時候
            for post in jd['data']:
                if 'message' in post:  #如果有發文資料
                    corpus += jieba.cut(post['message'])  #將發文資料切割並加到corpus的list裡面
            res = requests.get(jd['paging']['next'])   #繼續下一頁
            jd = res.json() #將資料轉成json

        for word in corpus:   #計算關鍵字出現次數
            if word not in dic:
                dic[word] = 1   #如果沒有出現則設成1
            else:
                dic[word] += 1  #如果已經出現則將內容+1

        sorted_word = sorted(dic.items(), key=operator.itemgetter(1), reverse=True) #以Key排序並以出現次數做降冪排列

        for ele in sorted_word:
            if len(ele[0]) >= 2:   #只印出Key長度>2的資料
                arr += [ele[0], ele[1]]
                print(ele[0], ele[1])
                ws.append(arr)
                arr=[]
        wb.save('臉書關鍵字.xlsx')
    else:
        print('token 已過期')