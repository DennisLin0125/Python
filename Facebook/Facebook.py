import requests
import jieba
import operator

url="https://graph.facebook.com/v15.0/me/posts?access_token="
token="EAAP1quLZAFo4BALDnA4WvWlmUdy1syRZBfE3c5t1oZBTZCqARtv1hE5z3H1ZBzPL5F5qfbWKzyTNl3yuqdvZAjF29WM0qssbAayS2LsgEtgb5x4HztofOzZCl6ZALbA0rYfMDStV2RadjBQ0pwhq5XndOBCBOMueG9MgpiMhdpv8FYMTmKP0mNanFizbzwY84ThVtgwVRoibxTeBMZBweGINRzOc1bj88NurrgBKrGflSHUZAzUaecjLu6"

res = requests.get(url=url+token)
jd = res.json()

corpus=[]
dic={}
if __name__ == "__main__":
    if res.status_code == requests.codes.ok:
        while 'paging' in jd:
            for i in jd['data']:
                if 'message' in i:
                    corpus += jieba.cut(i['message'])
            res = requests.get(jd['paging']['next'])
            jd = res.json()

        for i in corpus:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        sorted_word = sorted(dic.items(),key=operator.itemgetter(1),reverse=True)

        for ele in sorted_word:
            if len(ele[0])>=2:
                print(ele[0],ele[1])
    else:
        print('token 已過期')