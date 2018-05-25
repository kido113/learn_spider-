# -*- coding: utf-8 -*-



# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sys
import importlib
importlib.reload(sys)


class City58Pipeline(object):

    def open_spider(self,  spider):
        self.file = open('58_chuzu.txt','w',encoding='utf-8')
        print('已打开文件')

    def process_item(self, item, spider):
        line = '{}\n'.format(json.dumps(dict(item),ensure_ascii=False))

        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
        print('已关闭文件')