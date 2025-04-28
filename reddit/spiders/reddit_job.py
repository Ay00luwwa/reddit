import scrapy


class RedditJobSpider(scrapy.Spider):
    name = "reddit_job"
    allowed_domains = ["reddit.com"]

    start_urls = ['https://www.reddit.com/r/funny/']

    def parse(self, response):
        print (response.css("a.title::text").extract())
        print (response.css("a.title::attr(href)").extract())
        print (response.css("div.score.unvoted::attr(title)").extract())

        for item in zip(titles, hrefs, scores):

            new_item = RedditItem()
            
            new_item['title'] = item[0]
            new_item['url'] = item[1]
            new_item['score'] = item[2]
            
            yield new_item
