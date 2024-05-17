import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css("div.lsooF")
        for light in lights:
            yield {
                "name": light.css('div.lsooF span::text').get(),
                "url": light.css('a[class="ui-GPFV8 qUioe ProductName ActiveProduct"]').attrib["href"],
                "price": light.css('span[data-testid="price"]::text').get()
            }
