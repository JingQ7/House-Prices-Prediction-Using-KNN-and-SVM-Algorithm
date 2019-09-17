# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RewhouseItem(scrapy.Item):
    price = scrapy.Field()
    sqft = scrapy.Field()
    addr = scrapy.Field()
    link = scrapy.Field()
