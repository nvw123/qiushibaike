# -*- coding: utf-8 -*-
import scrapy
from ..items import QiubaiItem,OtherItem

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'

    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/8hr/page/1/']

    def parse(self, response):
        qiubai = QiubaiItem()
        other = OtherItem()
        divs = response.xpath('//div[@class="col1"]/div')
        for item in divs:
            qiubai['name'] = self.strip11(item.xpath('.//h2/text()').get())
            qiubai['content'] = self.strip11(item.xpath('.//div[@class="content"]/span/text()').get())
            other['comment'] = self.strip11(item.xpath('.//span[@class="stats-comments"]//i/text()').get())
            other['vote'] = self.strip11(item.xpath('.//span[@class="stats-vote"]/i/text()').get())
            # print(qiubai, other)
            # print(qiubai)
            yield qiubai
            yield other

    def strip11(self, num):
        if num:
            return num.strip()

