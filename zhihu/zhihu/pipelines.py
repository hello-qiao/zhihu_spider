# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class ZhihuPipeline(object):
    def process_item(self, item, spider):
        OutputFile = open('zhihu.csv', 'ab')
        writer = csv.writer(OutputFile)
        writer.writerow([item['url'].encode('utf-8'), item['title'].encode('utf-8')])
        # print item

        OutputFile.close()




