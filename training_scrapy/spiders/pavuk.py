import scrapy
from training_scrapy.items import PavukScrapyItem


class PavukSpider(scrapy.Spider):
    name = "pavuk"
    start_urls = [
        "https://platonov1727.ru/blog/",
    ]

    def parse(self, response):
        # Извлекаем ссылки на посты
        post_links = response.css("h4 a::attr(href)").getall()

        # Заходим на каждую статью
        for link in post_links:
            yield response.follow(link, self.parse_post)

        # Переходим на следующую страницу, если она есть
        next_page = response.css("a.page-link::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_post(self, response):
        data = {
            "title": response.css("h1::text").get(),  # Заголовок статьи
            "url": response.url,  # Ссылка на страницу
            "author": response.css("p.text-muted::text")
            .get()
            .split()[-1],  # Автор статьи
            "content": "".join(
                response.xpath(
                    '//div[@class="post-content mb-5"]//text()'
                ).getall()
            ),
        }
        yield PavukScrapyItem(data)
