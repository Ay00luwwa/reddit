import scrapy


class RedditJobSpider(scrapy.Spider):
    name = "reddit_job"
    allowed_domains = ["reddit.com"]
    start_urls = ["https://reddit.com"]

    def parse(self, response):
        pass
        