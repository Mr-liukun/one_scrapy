# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class OneScrapyPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect("172.17.0.2", "root", "root", "onedb")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into pachong (name) values('%s')" % (item["title"])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
