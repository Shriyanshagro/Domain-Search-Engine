# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class OneSpider(scrapy.Spider):
    name = "i"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
'http://www.biometrics.gov/',
'http://www.biometricsinstitute.org/pages/types-of-biometrics.html',
'http://support.microsoft.com/en-us/kb/246071',
'http://www.garykessler.net/library/fsc_stego.html',
'https://technet.microsoft.com/en-us/library/cc179103.aspx',
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
