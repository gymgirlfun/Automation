import scrapy

class BakerySpider(scrapy.Spider):
  name = 'bakery'
  start_urls = ['https://keewahsf.com/collections/in-store-pick-up-only',]

  def parse(self, response):
    for item in response.css('div.info'):
      yield {
        'name': item.css('span.title::text').get(),
        'price':  item.css('span.money::text').get()
      }

    next = response.css('span.next a::attr("href")').get()
    if next is not None:
      yield response.follow(next, self.parse)
