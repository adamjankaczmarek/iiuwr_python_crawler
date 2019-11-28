# coding: utf-8


class SearchIndex:

    def __init__(self):
        self.token_to_document_index = {}

    def serialize(self, output_path):
        pass

    def deserialize(self, input_path):
        pass

    @staticmethod
    def from_file(input_file):
        return SearchIndex()