import scrapy
from scrapy_selenium import SeleniumRequest


class SmartphonesSpider(scrapy.Spider):
    name = "smartphones"
    start_urls = [
        'https://www.daraz.pk/smartphones/',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse_result)

    def parse_result(self, response):
        for sp in response.selector.css('div.c2prKC'):
            yield {
                'title': sp.css('.c16H9d > a::text').get(),
                'price': sp.css('.c3gUW0 > span::text').get(),
                'discount': sp.css('span.c1hkC1::text').get(),
                'rating': 1,
                'ratings': 1
            }

    def parse(self, response):
        for sp in response.css('div.c2prKC'):
            yield {
                'title': sp.css('.c16H9d > a::text').get(),
                'price': sp.css('.c3gUW0 > span::text').get(),
                'discount': sp.css('span.c1hkC1::text').get(),
                'rating': 1,
                'ratings': 1
            }

        # yield from response.follow_all(css='ul.pager a', callback=self.parse)
