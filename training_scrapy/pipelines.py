from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from training_scrapy.db import Post, Base


class TrainingScrapyPipeline:
    def process_item(self, item, spider):
        return item


class PostsToDBPipeline:

    def open_spider(self, spider):
        engine = create_engine("sqlite:///sqlite.db")
        Base.metadata.create_all(engine)
        self.session = Session(engine)

    def process_item(self, item, spider):
        post = Post(
            title=item["title"],
            author=item["author"],
            content=item["content"],
            url=item["url"],
        )
        self.session.add(post)
        self.session.commit()
        return item

    def close_spider(self, spider):
        self.session.close()
