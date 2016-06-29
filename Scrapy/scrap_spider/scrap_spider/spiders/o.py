# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class OneSpider(scrapy.Spider):
    name = "o"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
'http://cs.stanford.edu/people/eroberts/courses/soco/projects/2000-01/risc/whatis/',
'http://www.gammassl.co.uk/research/chinesewall.php',
'http://www.softpanorama.org/Access_control/Security_models/',
'http://www.openpgp.org/',
'http://www.quadibloc.com/crypto/jscrypt.htm',
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
