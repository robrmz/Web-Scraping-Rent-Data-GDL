import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import requests


class VivaSpider(CrawlSpider):
    name = 'VivaAnuncios'
    allowed_domain = ['www.vivanuncios.com.mx']
    start_urls = ['https://www.vivanuncios.com.mx/s-departamentos-en-renta/guadalajara/v1c1300l14822p1']
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('div.desktop-pagination',)), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        #productos
        for name in response.xpath("//*[@id='tileRedesign']/div"):
            yield {
                'Colonia' : name.xpath('normalize-space(div[4]/b/text())').get(),
                'Precio' : name.xpath('normalize-space(span/span/text())').get(),
                'Descripción': name.xpath('normalize-space(div[5]/a/text())').get(),
            }
