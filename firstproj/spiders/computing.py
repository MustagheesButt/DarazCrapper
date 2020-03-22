import scrapy
from scrapy_selenium import SeleniumRequest
import re


# 273999 items on daraz in this category

class ComputingSpider(scrapy.Spider):
    name = "computing"
    start_urls = [
        'https://www.daraz.pk/computing/',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse_result)

    def parse_result(self, response):
        for sp in response.selector.css('div.c2prKC'):
            title    = sp.css('.c16H9d > a::text').get()
            price    = sp.css('.c3gUW0 > span::text').get()
            discount = sp.css('span.c1hkC1::text').get() or "0%"
            rating   = len(sp.css('div.c2JB4x > i.c3EEAg').getall()) # c3EEAg => 1 star element
            ratings  = sp.css('div.c2JB4x > span.c3XbGJ::text').get() or 0

            # remove parenthesis around the number
            if ratings != 0:
                ratings = re.findall(r'\(([^()]+)\)', ratings)
            
            yield {
                'title': title,
                'price': price,
                'discount': discount,
                'rating': rating,
                'ratings': ratings
            }
        
        # find URLs for next pages and follow em
        for href in response.selector.css('li.ant-pagination-item > a::attr(href)').getall():
            if href is not None:
                yield SeleniumRequest(url=response.urljoin(href), callback=self.parse_result)
