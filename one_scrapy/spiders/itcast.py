# -*- coding: utf-8 -*-
import scrapy

from one_scrapy.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast' # 爬虫的识别名字，必须唯一
    allowed_domains = ['itcast.com'] # 域名范围，爬虫只会爬取这个域名下的网页
    start_urls = ['http://www.itcast.cn/'] # 爬虫的url列表

    def parse(self, response):
        context = response.xpath("/html/head/title/text()")
        it = ItcastItem()
        value = context.extract_first()
        it["title"] = value
        return it


