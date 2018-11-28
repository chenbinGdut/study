# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaHzwItem(scrapy.Item):
    # 发帖人昵称
    user_name = scrapy.Field()
    # 用户等级
    user_level = scrapy.Field()
    # 发帖时间
    create_time = scrapy.Field()
    # 使用的客户端
    client = scrapy.Field()