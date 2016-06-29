# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class OneSpider(scrapy.Spider):
    name = "a"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
'http://www.pcmag.com/article2/0,2817,2372364,00.asp',
'https://technet.microsoft.com/en-us/library/hh994558%28v=ws.10%29.aspx',
'https://technet.microsoft.com/en-us/library/hh994561(v=ws.10).aspx',
'https://technet.microsoft.com/en-us/library/dd883248(v=ws.10).aspx',
'https://technet.microsoft.com/en-us/library/cc755284(v=ws.10).aspx',
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
