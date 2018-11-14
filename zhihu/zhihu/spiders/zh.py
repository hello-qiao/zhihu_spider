# -*- coding: utf-8 -*-
import scrapy
from zhihu.items import ZhihuItem


class ZhSpider(scrapy.Spider):
    name = 'zh'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/question/']



    def start_requests(self):
        header = {
            'accept-language': ' zh-CN,zh;q=0.9',
            # 'accept-encoding': ' gzip, deflate, br',
            'accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'referer': ' https',
            'Pragma': ' no-cache',
            'Cache-Control': ' no-cache',
            'upgrade-insecure-requests': ' 1'
        }
        num = 22619469

        for i in range(1000000):
            page_num = num + i
            url = self.start_urls[0] + str(page_num)
            yield scrapy.Request(
                url = url,
                method='GET',
                headers = header,
                callback = self.parse,
                errback = self.error,
                meta = {'url':url},
            )




    def parse(self, response):
        # // *[ @ id = "root"] / div / main / div / div[1] / div[2] / div[1] / div[1] / h1  QuestionHeader-title
        name = response.xpath('//*[@class="QuestionHeader-title"]/text()')
        # print name[0].extract()
        item = ZhihuItem()
        item['title'] = response.xpath('//title/text()')[0].extract()
        item['url'] = response.meta.get('url')
        print item['url']
        # print response.xpath('//title/text()')[0].extract()
        yield item


    def error(self,failure):
        # print 'error'
        return