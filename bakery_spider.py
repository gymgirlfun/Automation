import scrapy

class BakerySpider(scrapy.Spider):
  name = 'bakery'
#   start_urls = ['https://keewahsf.com/collections/in-store-pick-up-only',]

# scrapy crawl bakery -a category=in-store-pick-up-only
  def __init__(self, category=None, *args, **kwargs):  
    super(BakerySpider, self).__init__(*args, **kwargs)
    self.start_urls = [f'https://keewahsf.com/collections/{category}',]
    
    
  def parse(self, response):
    for item in response.css('div.info'):
      yield {
        'name': item.css('span.title::text').get(),
        'price':  item.css('span.money::text').get()
      }

    next = response.css('span.next a::attr("href")').get()
    if next is not None:
      yield response.follow(next, self.parse)
