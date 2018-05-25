# -*- coding:utf-8 -*-

import requests
import pandas as pd
import time

headers = {
   'authorization':'Bearer 2|1:0|10:1522416552|4:z_c0|92:Mi4xWmQzNkFBQUFBQUFBb0NfS190UmREU1lBQUFCZ0FsVk5xSW1yV3dESWQ4MDJPNWRJejBaNVdmQ1pFTkM3OFVMN0R3|456b64fe2ab3b03a062b89aef84a6f50c742f62156afd56e313aca4894406a9d', #括号中填上你的authorization
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36', #括号中填上你的User-Agent
}

user_data = []
def get_user_data(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
        response= requests.get(url, headers = headers).json()['data']
        user_data.extend(response)
        print("正在爬取第%s页" % str(i+1))
        time.sleep(2)

if __name__ == '__main__':
    get_user_data(3)
    df = pd.DataFrame.from_dict(user_data)
    #print(response)
    #print(df.head())
    df.to_csv('user.csv',encoding='utf_8_sig')