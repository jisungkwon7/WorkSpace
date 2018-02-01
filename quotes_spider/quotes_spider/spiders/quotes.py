# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

from quotes_spider.items import QuotesSpiderItem
class QuotesSpider(Spider):
    name = 'quotes'
    # allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.xpath(
            '//*[@name="csrf_token"]/@value').extract_first()
        return FormRequest.from_response(response,
                                         formdata={'csrf_token' : token,
                                                   'password' : 'foobar',
                                                   'username' : 'barfoo'},
                                         callback=self.scrape_home_page)

    def scrape_home_page(self, response): #parse call back 하지 않아도 된다
        open_in_browser(response) #브라우저를 연다
        l = ItemLoader(item=QuotesSpiderItem(), response=response)

        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class = "tag-item"]/a/text()').extract()

        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)

        # quotes =response.xpath('//*[@class="quote"]')
        # for quote in quotes:
        #     text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        #     author = quote.xpath('.//*[@class = "author"]/text()').extract_first()
        #     tags_q = quote.xpath('.//*[@itemprop = "keywords"]/@content').extract_first()
        #
        #     l.add_value('text', text)
        #     l.add_value('author', author)
        #     l.add_value('tags_q', tags_q)
        return l.load_item()


        # next_page_url = response.xpath('//*[@class = "next"]/a/@href').extract_first()
        # absolute_next_page_url = response.urljoin(next_page_url)
        # yield scrapy.Request(absolute_next_page_url)

        # h1_tag = response.xpath('//h1/a/text()').extract_first()
        # tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        #
        # yield{'H1_tag': h1_tag, 'Tag': tags}
