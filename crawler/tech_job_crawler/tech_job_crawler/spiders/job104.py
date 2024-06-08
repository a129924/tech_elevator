from scrapy import Request, Spider
from scrapy.http import HtmlResponse

from ..items.job_104 import Job104Item


class Job104Spider(Spider):
    name = "job104"
    allowed_domains = ["104.com.tw"]
    start_urls = ["https://104.com.tw"]

    def parse(self, response: HtmlResponse):
        from ..utils.response import url_join

        search_url = url_join(
            response=response,
            path_param="/jobs/search",
            keyword="python",
        )

        self.logger.info(f"{search_url = }")

        yield response.follow(url=search_url, callback=self.parse_search_page)

    def parse_search_page(self, response: HtmlResponse):
        articles = response.css("#js-job-content > article")

        for article in articles:
            item = Job104Item()
            item["company_name"] = article.css("::attr(data-cust-name)").get()
            item["job_url"] = (
                f'https:{article.css("div > h2 > a::attr(href)").get().__str__()}'
            )

            self.logger.info(f"{item['company_name'] = }, {item['job_url'] = }")

            yield Request(
                url=item["job_url"], callback=self.parse_job_page, meta={"item": item}
            )

    def parse_job_page(self, response: HtmlResponse):
        item = response.meta["item"]

        # 将 HTML 内容保存到文件
        with open(f"debug.html_{item['company_name']}", "w", encoding="utf-8") as f:
            f.write(response.text)

        job_content = response.css(
            "p.mb-5.r3.job-description__content.text-break::text"
        ).get()
        work_address = "".join(response.css("span[data-v-e81f764d]::text").getall())
        salary = "".join(
            response.css("div.col.flex-1.text-primary.h3 > span::text").getall()
        )
        other_condition = response.css(
            "div.col.p-0.job-requirement-table__data > p.t3.m-0::text"
        ).get()

        self.logger.info(f"job_content: {job_content}")
        self.logger.info(f"work_address: {work_address}")
        self.logger.info(f"salary: {salary}")
        self.logger.info(f"other_condition: {other_condition}")

        item["job_content"] = job_content
        item["work_address"] = work_address
        item["salary"] = salary
        item["other_condition"] = other_condition

        yield item
