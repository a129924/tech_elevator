from scrapy.http import HtmlResponse


__all__ = ["url_join"]


def url_join(response: HtmlResponse, path_param: str, **query_params: str) -> str:
    from urllib.parse import urlencode

    url = response.urljoin(path_param)
    query_url = f"/?{urlencode(query_params)}" if query_params else ""

    return f"{url}{query_url}"
