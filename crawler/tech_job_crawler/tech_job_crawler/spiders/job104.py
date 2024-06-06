from scrapy import Spider
from scrapy.http import HtmlResponse


class Job104Spider(Spider):
    name = "job104"
    allowed_domains = ["104.com.tw"]
    start_urls = ["https://104.com.tw"]

    def parse(self, response: HtmlResponse):
        from ..utils.response import url_join

        search_url = url_join(
            response=response,
            path_param="/obs/search",
            keyword="python",
        )

        self.logger.info(f"{search_url = }")

        yield response.follow(url=search_url, callback=self.parse_search_page)

    def parse_search_page(self, response: HtmlResponse):
        articles = ...
        ...
