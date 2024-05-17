import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css("div.lsooF")
        parsed_data = []
        for light in lights:
            yield
            parsed_data.append({
                "name": light.css('div.lsooF span::text').get(),
                "url": light.css('a[class="ui-GPFV8 qUioe ProductName ActiveProduct"]').attrib["href"],
                "price": light.css('span[data-testid="price"]::text').get()
            })

        with open("light.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "url", "price"])
            writer.writeheader()
            writer.writerows(parsed_data)
