# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class OneSpider(scrapy.Spider):
    name = "f"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
'https://technet.microsoft.com/en-us/library/cc732077(v=ws.10).aspx',
'https://technet.microsoft.com/en-us/library/cc772066(v=ws.10).aspx',
'https://twitter.com/bruce_schneier',
'http://www.isaccouncil.org/memberisacs.html',
'https://tools.ietf.org/',
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
