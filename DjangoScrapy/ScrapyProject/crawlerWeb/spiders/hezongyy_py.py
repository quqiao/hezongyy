# -*- coding: utf-8 -*-
import scrapy
from crawlerWeb.items import CrawlerwebItem


class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["hezongyy.com"]
    start_urls = ['https://www.hezongyy.com/puyao.html']

    def parse(self, response):
        item = CrawlerwebItem()
        quotes = response.xpath('//*[@id="datu"]/div/ul')
        for quote in quotes:
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()

            item['text'] = text
            item['author'] = author
            item['tags'] = tags

            yield item

        # next = response.css('.pager .next a::attr(href)').extract_first()
        # url = response.urljoin(next)
        # yield scrapy.Request(url=url, callback=self.parse)