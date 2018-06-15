# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    table_name = 'vote_content '
    name = scrapy.Field()
    content = scrapy.Field()

class OtherItem(scrapy.Item):
    table_name = 'vote_counts'
    vote = scrapy.Field()
    comment = scrapy.Field()
