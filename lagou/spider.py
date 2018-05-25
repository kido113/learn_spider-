from pymongo import MongoClient
import requests
import time
from fake_useragent import UserAgent

client = MongoClient()
db = client.lagou #创建一个lagou数据库
my_set = db.job #创建job集合

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

headers = {
    'Cookie': 'user_trace_token=20170927131307-e119a1dbb0d4434e931b6f19f014fc83; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1506489189; _ga=GA1.2.230512144.1506489189; LGUID=20170927131308-8ce65cab-a342-11e7-92ef-5254005c3644; _gid=GA1.2.75505639.1522495441; JSESSIONID=ABAAABAAAFCAAEGADFB1AE24E416E4B0253C4198581E279; SEARCH_ID=d7e01b4d62c54581b57de51d425feb07; LGSID=20180401154923-318da75a-3581-11e8-abd8-525400f775ce; PRE_UTM=; PRE_HOST=static.dcxueyuan.com; PRE_SITE=https%3A%2F%2Fstatic.dcxueyuan.com%2Fcontent%2Fdisk%2Ftrain%2Fother%2F70b2c405-138b-4862-ad49-138656aef0d6.html; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; LGRID=20180401154923-318daa7b-3581-11e8-abd8-525400f775ce; TG-TRACK-CODE=search_code',
    'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',

}  # 填入对应的headers信息

def get_job_info(page):
    for i in range(page):

        payload = {
                        'first':'true',
                        'pn':i+1,
                        'kd':'爬虫',
                        }


        ua = UserAgent()
        headers['User-Agent']=ua.random
        response = requests.post(url, data = payload, headers = headers) #使用POST方法请求数据，加上payload和headers信息
        print(response.status_code)
        print("正在爬取第%s页" % str(i+1))
        time.sleep(5)
        my_set.insert(response.json()['content']['positionResult']['result']) #把对应的数据保存到MOngoDB

if __name__ == '__main__':
    get_job_info(5)