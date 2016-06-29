# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class OneSpider(scrapy.Spider):
    name = "one"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
'http://www.wisegeek.com/what-is-tls.htm',
'http://www.governmentsecurity.org/',
'http://www.wired.com/category/threatlevel',
'http://www.austinfosec.com',
'http://www.wired.com/2014/11/hacker-lexicon-whats-dark-web/'
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        for url in hxs.select('//a/@href').extract():
            if not ( url.startswith('http://') or url.startswith('https://') ):
                url = response.urljoin(url)
            # print url
            filename = response.url.split("/")[-2] + '.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            pass
            yield Request(url, callback=self.parse)
