# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Job104Item(Item):
    company_name = Field()
    job_url = Field()
    job_content = Field()
    work_address = Field()
    salary = Field()
    other_condition = Field()
