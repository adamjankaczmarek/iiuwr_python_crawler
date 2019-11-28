# coding: utf-8
from .index import SearchIndex


class SearchEngine:

    def __init__(self, search_index: SearchIndex):
        self.search_index = search_index
        # Create BM25 or TFIDF model

    def __getitem__(self, item):
        pass