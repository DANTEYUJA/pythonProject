import requests

#coding:utf-8

url = 'https://api.sumt.cn/api/rand.tbimg.php'

params = {
    'token': 'Q5g436JwHVPoX14PgAxl0Yxq',
    'format': 'json',
}

res = requests.get(url, params=params).json()
print(res)
