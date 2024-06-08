# Scrapy settings for tech_job_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "tech_job_crawler"

SPIDER_MODULES = ["tech_job_crawler.spiders"]
NEWSPIDER_MODULE = "tech_job_crawler.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
DUPEFILTER_DEBUG = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    # "Cookie": "_gcl_au=1.1.2091530806.1714576251; _ga=GA1.1.1401769098.1714576251; _ga=GA1.4.1401769098.1714576251; luauid=283146280; _clck=7v2sie%7C2%7Cflv%7C0%7C1599; c_job_algo_exp_poc=C; c_job_algo_exp_date_poc=G; _hjSessionUser_3218023=eyJpZCI6ImNkNTYyYjZlLWJiY2QtNWQ2NS05N2U4LTgxMTE4MmI0Y2RhMSIsImNyZWF0ZWQiOjE3MTYwNDI5NzEyMjIsImV4aXN0aW5nIjp0cnVlfQ==; cust_same_ab=1; job_same_ab=1; bprofile_history=%5B80710658000%2C130000000042110%2C4541302000%2C12304443000%5D; c_job_view_job_info_nabi=6zczh%2C2007001012; _hjSession_3218023=eyJpZCI6IjQ2OWMxOWEzLTI2MmEtNDc0Ny1iOWEyLWJkOTQzNGE3ZDYzYiIsImMiOjE3MTc2ODMzNTg4NTcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; lup=283146280.4726611507047.4623532291991.1.4640712161167; lunp=4623532291991; dtCookie=v_4_srv_3_sn_968D02A0AE8D98CA7CF396B8E3229F05_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0; _ga_FJWMQR9J2K=GS1.1.1717692503.9.1.1717692503.60.0.0; _ga_WYQPBGBV8Z=GS1.4.1717692503.8.1.1717692503.60.0.0; _ga_W9X1GB1SVR=GS1.1.1717692503.9.1.1717692503.60.0.0",
    "Host": "www.104.com.tw",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.3",
    "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "tech_job_crawler.middlewares.TechJobCrawlerSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "tech_job_crawler.middlewares.TechJobCrawlerDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "tech_job_crawler.pipelines.TechJobCrawlerPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
