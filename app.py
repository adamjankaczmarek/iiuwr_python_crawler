# coding: utf-8
import os
import sys
from crawlers import AsyncCrawler
from search_engine.engine import SearchIndex, SearchEngine

BASE_URL = "https://en.wikipedia.org"
MAX_DEPTH = 5


def create_search_index(index_file):
    crawler = AsyncCrawler()
    document_to_list_of_tokens = crawler.crawl(BASE_URL, MAX_DEPTH)
    index = SearchIndex(document_to_list_of_tokens)
    index.serialize(index_file)


def initialize_search_index(index_file, force_reload):
    if force_reload or not os.path.exists(index_file):
        create_search_index(index_file)
    return SearchIndex.from_file(index_file)


def main(index_file, force_reload):
    index = initialize_search_index(index_file, force_reload)
    engine = SearchEngine(index)
    while True:
        try:
            q = input()
            print(engine[q])
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    index_file = sys.argv[1]
    force_reload = False
    main(index_file, force_reload)
