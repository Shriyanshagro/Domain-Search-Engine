# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class OneSpider(scrapy.Spider):
    name = "k"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
'https://cryptoworks21.uwaterloo.ca/cryptography',
'http://www.fortinet.com',
'https://crackstation.net/hashing-security.htm',
'http://www.enterprisedb.com/docs/en/9.3/pg/sql-security-label.html',
'http://www.arubanetworks.com/products/security/',
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
