import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from mp.items import MpItem


class ForsaleSpider(CrawlSpider):
    name = "forsale"
    allowed_domains = ["https://www.mountainproject.com/"]
    start_urls = [
        'https://www.mountainproject.com/forum/103989416/for-sale-for-free-want-to-buy'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=False),)

    def parse_item(self, response):
        item_links = response.css('.new-indicator > .detailsLink::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        title = response.css('h1::text').extract()[0].strip()
        #price = response.css('.pricelabel > strong::text').extract()[0]

        item = OlxItem()
        item['title'] = title
        #item['price'] = price
        item['url'] = response.url
        print(title+' '+response.url)
        yield item
