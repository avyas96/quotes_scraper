import scrapy
import json

base_url = 'https://quotes.toscrape.com/api/quotes?page={}'
class QuotesScrollSpider(scrapy.Spider):
    name = "quotes_scroll"
    start_urls = [base_url.format(1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data["quotes"]:
            yield {
                'text': quote["text"],
                'author': quote["author"]["name"],
            }

        current_page = data["page"]
        if data["has_next"]:
            next_page_url = base_url.format(current_page+1)
            yield scrapy.Request(next_page_url)