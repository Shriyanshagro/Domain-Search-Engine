# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class OneSpider(scrapy.Spider):
    name = "p"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
'http://search.cpan.org/dist/Crypt-Loki97/Loki97.pm',
'https://www.fastmail.com/help/technical/ssltlsstarttls.html',
'http://www.ietf.org/rfc/rfc4880.txt',
'https://tools.ietf.org/html/rfc2595',
'http://www.pcmag.com/article2/0,2817,2407168,00.asp',
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
