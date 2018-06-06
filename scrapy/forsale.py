# -*- coding: utf-8 -*-
import scrapy


class ForsaleSpider(scrapy.Spider):
    name = 'forsale'
    allowed_domains = ['https://www.mountainproject.com/forum/103989416/for-sale-for-free-want-to-buy']
    start_urls = ['http://https://www.mountainproject.com/forum/103989416/for-sale-for-free-want-to-buy/']

    def parse(self, response):
        pass
