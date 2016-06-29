# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class OneSpider(scrapy.Spider):
    name = "u"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
'http://www.esslsecurity.com/',
'http://stackoverflow.com/questions/tagged/security',
'http://docs.saltstack.com/en/latest/',
'https://saltthepass.com/#help-about',
'http://crypto.stackexchange.com/',
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
