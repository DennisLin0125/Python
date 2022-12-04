import requests
import jieba

url="https://graph.facebook.com/v15.0/me/posts?access_token="
token="EAAP1quLZAFo4BAABRAJuQx35wMvKqxs247tpv0HBxoLWU8upPwZCDT1bdLTVeu85RFGCZCNN0jdcvbdbDZCKCQhF3sLMu3ZABbF8xDnBI3ctI4ZC6lIMZAAwsyFiEKIl80yM8czIW6CJ9nELy8U6xWh3ZBzBokdgkZAdoqtjirTZCXZBiFBZCjoX6YgZAoc3IeKcqfAfVoxhpofRQzttSs4f3UwUrSSWNbyvBDZBDNdSZBLvKfsxnBilw7ZAbE9G"

res = requests.get(url=url+token)
jd = res.json()

if __name__ == "__main__":
    if res.status_code == requests.codes.ok:
        while 'paging' in jd:
            for i in jd['data']:
                if 'message' in i:
                    print(i['message'])
                    print('--------------------------------')
            res = requests.get(jd['paging']['next'])
            jd = res.json()
    else:
        print('token 已過期')