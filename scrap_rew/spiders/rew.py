# -*- coding: utf-8 -*-
import scrapy
from rewhouse.items import RewhouseItem
from scrapy.http import Request

class RewSpider(scrapy.Spider):
    name = 'rew'
    allowed_domains = ['www.rew.ca']
    #start_urls = ['https://www.rew.ca/properties/areas/toronto-on']

    def start_requests(self):
        start_url = 'https://www.rew.ca/properties/areas/toronto-on'
        yield Request(url=start_url, callback=self.parse)

    def parse(self, response):
        item = RewhouseItem()
        item['price'] = response.xpath('//div[@class="displaypanel-title hidden-xs"]/text()').extract()
        item['addr'] = response.xpath('//div[@class="displaypanel-body"]/a/@title').extract()
        item['link'] = response.xpath('//div[@class="displaypanel-body"]/a/@href').extract()
        yield item
        for i in range(2, 25):
            rew_url = 'https://www.rew.ca/properties/areas/toronto-on/page/' + str(i)
            yield Request(url=rew_url, callback=self.parse)
