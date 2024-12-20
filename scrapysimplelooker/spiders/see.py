import scrapy


class SeeSpider(scrapy.Spider):
    name = "see"
    # allowed_domains = ["example.com"]
    start_urls = ["https://www.pagesjaunes.fr/annuaire/region/auvergne-rhone-alpes/supermarches-hypermarches"]

    def parse(self, response):
        print(response)
        
