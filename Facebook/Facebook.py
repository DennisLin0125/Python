import requests
import jieba
import operator

url = "https://graph.facebook.com/v15.0/me/posts?access_token="
token = "EAAP1quLZAFo4BAOcJYLzU5nzNb721j29jzOkrVPsO440GS3ww4Md7llTtyLYSppYUS4oW1mVYeVMHfFQSJVjsu15oAzfm07P1THHvwrEvHZB7lwE7ejMqZAxXbMEwzNgziqgz8IXEF2SQwNZAYOw8siJExVSHjXxyZC7tzSqLMIswXmC21B2AzAs9qhw8jyMzX5SAsSXjbmO5WTqVhIIQ09vanibrtkFqZBKHlffHDoqqp7ZCoV915r"

res = requests.get(url=url+token)
jd = res.json()

corpus=[]
dic={}
if __name__ == "__main__":
    if res.status_code == requests.codes.ok:
        while 'paging' in jd:
            for post in jd['data']:
                if 'message' in post:
                    corpus += jieba.cut(post['message'])
            res = requests.get(jd['paging']['next'])
            jd = res.json()

        for word in corpus:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1

        sorted_word = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

        for ele in sorted_word:
            if len(ele[0]) >= 2:
                print(ele[0], ele[1])
    else:
        print('token 已過期')