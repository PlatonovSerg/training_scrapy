BOT_NAME = "training_scrapy"

SPIDER_MODULES = ["training_scrapy.spiders"]
NEWSPIDER_MODULE = "training_scrapy.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


FEEDS = {
    "posts_text_%(time)s.csv": {
        "format": "xml",
        "fields": ["url", "title", "content"],
        "overwrite": True,
    },
    "quotes_author_%(time)s.csv": {
        "format": "csv",
        "fields": ["author"],
        "overwrite": True,
    },
}

ITEM_PIPELINES = {
    "training_scrapy.pipelines.PostsToDBPipeline": 300,
}
