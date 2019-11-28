from abc import ABC, abstractmethod


class BaseCrawler(ABC):

    @abstractmethod
    def  __init__(self):
        pass

    @abstractmethod
    def crawl(self, start_url, max_depth):
        pass


