# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import City58Item
from scrapy.http import Request
class City58TestSpider(scrapy.Spider):
    name = 'city58_test'
    allowed_domains = ['58.com']
    start_urls = ['http://hf.58.com/chuzu/']

    def parse(self, response):
        jpy = PyQuery(response.text)
        li_list = jpy('body > div.mainbox > div.main > div.content > div.listBox > ul > li')
        for it in li_list.items():
            a_tag = it('div.des > h2 > a')
            item = City58Item()
            item['name'] = a_tag.text()
            item['url'] = a_tag.attr('href')
            item['price'] = it('div.listliright > div.money > b').text()
            yield item

        req = response.follow('/chuzu/pn2/',callback = self.parse)
        yield req

        test_req1 = Request('http://hf.58.com/chuzu/pn3',
                            callback=self.parse,
                            errback=self.error_back,
                            priority=10)

        test_req2 = Request('http://58.com',
                            callback=self.parse,
                            errback=self.error_back,
                            priority=10,
                            meta={'dont_redirect':True})

        yield test_req1
        yield test_req2

    def error_back(selfself,e):
        _ = self
        print(e)
        print("我报错了")