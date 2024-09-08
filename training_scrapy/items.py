# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class TrainingScrapyItem(scrapy.Item):
#     title = scrapy.Field()
#     url = scrapy.Field()
#     author = scrapy.Field()
#     content = scrapy.Field()


class PavukScrapyItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
