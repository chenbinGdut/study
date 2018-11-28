# -*- coding: utf-8 -*-
import scrapy
from ..items import TiebaHzwItem


class HzwSpider(scrapy.Spider):
    name = 'hzw'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=0']
    def parse(self, response):
        """找到起始页的所有发帖"""
        # 帖子url
        url_list = response.xpath('//ul[@id="thread_list"]//a/@href').re(r'/p/\d*')
        for url in url_list:
            url = 'https://tieba.baidu.com' + url
            yield scrapy.Request(url, callback=self.parse_tie)

        # 获取下一页url
        next_url = response.xpath('//div[@id="frs_list_pager"]/a[text()="下一页>"]/@href')
        num = next_url.re_first('pn=(\d*)')
        # 爬取前一百页
        if int(num) < 5000:
            next_url = 'https:' + next_url.extract_first()
            print(next_url)
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_tie(self, response):
        # 发帖人的信息
        # 提取发帖时间的样式
        pat = r'\d{2}:\d{2}'
        author_list = response.xpath('//div[@class="p_postlist"]/div')
        for author in author_list:
            info = TiebaHzwItem()
            name = author.xpath('.//li[@class="d_name"]/a/text()').extract_first()
            info['user_name'] = name
            info['user_level'] = author.xpath('.//div[@class="d_badge_lv"]/text()').extract_first()
            info['create_time'] = author.xpath('.//span[@class="tail-info"]/text()').re_first(pat)
            info['client'] = author.xpath('.//span[@class="tail-info"]/a/text()').extract_first()
            yield info

        # 贴子下一页url
        next_url = response.xpath('//li[@class="l_pager pager_theme_5 pb_list_pager"]/a[text()="下一页"]')
        if next_url:
            next_url = 'https://tieba.baidu.com' + next_url.xpath('./@href').extract_first()
            yield scrapy.Request(next_url, callback=self.parse_tie)
