# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class OneSpider(scrapy.Spider):
    name = "r"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
'https://www.kuppingercole.com/blog/kuppinger/information-rights-management-microsoft-gives-it-a-new-push-just-in-time-to-succeed',
'http://www.cisco.com/c/en/us/td/docs/ios/sec_data_plane/configuration/guide/12_4/sec_data_plane_12_4_book.html',
'https://www.freebsd.org/doc/handbook/index.html',
'http://www.cgisecurity.com/owasp/html/index.html',
'http://csrc.nist.gov/',
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
